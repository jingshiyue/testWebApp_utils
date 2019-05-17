# -*- coding:utf-8 -*- 
import os 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(parentdir)
from utils.config import config
from utils.mylog import mylog
import pymysql




class db:
    #----------------数据库必须事先存在，否则报错------------------------------------------------------
    def __init__(self):
        """"""
        cfg = config()
        host=cfg.get_database_parm("host")
        port=int(cfg.get_database_parm("port"))
        username=cfg.get_database_parm("username")
        password=cfg.get_database_parm("password")
        #database=config.get_database_parm("database")  
        #database = db_name
        
        try:
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=username,
                                              password=password,
                                              #db=database,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
            logger.debug("connect mysql successfully")
            self.cursor = self.connection.cursor()
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            
        
    def create_db(self,db_name):
        """
        create database 数据库名称 default character set utf 8
        """
        #cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %DB_NAME)
        real_sql = "create database if not exists %s" %db_name
        with self.cursor as cur:
            self.cursor.execute(real_sql)
            logger.debug(real_sql)
        self.connection.commit()    
                    
    #查询一条数据
    def search_one(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        result = json.dumps(result)
        return result        
        
        
        
    #----------------------------------------------------------------------
    def show_databases(self):
        """"""
        table_name = self.cursor.description
        return table_name
    
        
    #----------------------------------------------------------------------
    def drop_databases(self,db_name):
        """"""
        #cursor.execute('DROP DATABASE IF EXISTS %s' %DB_NAME)
        db = connect_db()
        real_sql = "drop database if exists %s" %db_name
        with self.cursor as cur:
            self.cursor.execute(real_sql)
            logger.debug(real_sql)
        self.connection.commit()        
        
    #----------------------------------------------------------------------
    def create_table(self,db_name,tb_name):
        """"""
        #cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' %TABLE_NAME)
        real_sql = 'create table %s (id int primary key,name varchar(30))' %tb_name
        #db.cursor().execute("use %s" %db_name)
        self.connection.select_db(db_name)
        with self.cursor as cur:
            self.cursor.execute(real_sql)
            logger.debug(real_sql)
        self.connection.commit()                      
        
    #----------------------------------------------------------------------
    def get_table_name():
        """"""
        db = connect_db()
        name = db.cursor().fetchone()
        return name
    
            
    #----------------------------------------------------------------------
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        #print(table_name)
        #print(table_data)
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        #print(key)
        #print(value)
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            print(table, data)
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()
        


if __name__ == '__main__':
    mylog = mylog()
    logger = mylog.get_log().get_logger()
    logger.debug("i am ok")    
    #connect_db()
    db= db()
    #db.create_db("ss")
    db.create_table('ss', 'test_name')
    #print(n)