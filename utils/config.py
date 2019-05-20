# -*- coding:utf-8 -*- 
import configparser
import os
import codecs
import yaml
########################################################################
class config:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #config_file = parentdir + "\config.ini"
        config_file = os.path.join(parentdir,"config.ini")
        try:
            fd = open(config_file)
        except:
            print("config file not exist...")
        data = fd.read()
        
            #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()       
                
        #print(config_file)
        self.cf = configparser.ConfigParser()
        self.cf.read(config_file)        
        
    #----------------------------------------------------------------------
    def get_email_parm(self,parm):
        """"""
        value = self.cf.get("EMAIL",parm)
        return value
        
    #----------------------------------------------------------------------
    def get_http_parm(self,parm):
        """"""
        value = self.cf.get("HTTP",parm)
        return value
        
    #----------------------------------------------------------------------
    def get_headers_parm(self,parm):
        """"""
        value = self.cf.get("HEADERS",parm)
        return value
        
    #----------------------------------------------------------------------
    def get_database_parm(self,parm):
        """"""
        value = self.cf.get("DATABASE",parm)
        return value
    
########################################################################
class yaml_conf:
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        file = r"..\data\desired_caps.yaml"
        yf = open(file,'r')
        self.data=yaml.load(yf)
        
        self.desired_caps={}
        self.desired_caps['platformName']=self.data['platformName']
        self.desired_caps['platformVersion']=self.data['platformVersion']
        self.desired_caps['deviceName']=self.data['deviceName']
        self.desired_caps['app']=self.data['app']
        self.desired_caps['appPackage']=self.data['appPackage']
        self.desired_caps['appActivity']=self.data['appActivity']
        self.desired_caps['noReset']=self.data['noReset']
        self.desired_caps['automationName']=self.data['automationName']
        #self.driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)        
        

if __name__ == '__main__':
    #config = config()
    #value = config.get_headers_parm('token_v')
    #print(value)
    yaml_data = yaml_conf()  #automationName
    print(yaml_data.desired_caps['automationName'])
    