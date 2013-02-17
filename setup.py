
from distutils.core import setup
import py2exe

options = {"py2exe":  
            {   "compressed": 1,  
                "optimize": 2,  
                "bundle_files": 1 
            }  
          }  
setup(     
    description = "SimpleRemindern",  
    name = "SimpleReminder",  
    options = options,  
    
    zipfile=None,  
    windows=[{"script": "SimpleReminder.py"}],    
    )  