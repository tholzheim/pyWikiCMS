'''
Created on 2020-12-31

@author: wf
'''
import os

class Site(object):
    '''
    migrated from:
    https://github.com/BITPlan/com.bitplan.wikifrontend/blob/master/src/main/java/com/bitplan/wikifrontend/Site.java
    '''

    def __init__(self,name:str,defaultPage:str="Main Page",lang:str="en"):
        '''
        Constructor
        
        Args:
            name(str): the name of this site
            defaultPage(str): the default Page of this site
            lang(str): the default language of this site
        '''
        self.name=name
        self.defaultPage=defaultPage
        self.lang=lang
        
    def stateSymbol(self,b:bool)->str:
        '''
        return the symbol for the given boolean state b
        
        Args:
            b(bool): the state to return a symbol for
            
        Returns:
            ✅ for True and ❌ for false
        '''
        symbol="✅" if b else "❌"
        return symbol
        
    def configure(self,config:dict):
        '''
        configure me from the given configuration
        Args:
            config(dict): the configuration to use
        '''
        self.wikiId=config['wikiId']
        self.defaultPage=config['defaultPage']
        self.template=config['template']
        
    def checkApacheConfiguration(self)->str:
        '''
        check the apache configuration and return an indicator symbol
        '''
        path="/etc/apache2/sites-available/%s.conf" % self.name
        confExists=os.path.isfile(path)
        stateSymbol=self.stateSymbol(confExists)
        return stateSymbol