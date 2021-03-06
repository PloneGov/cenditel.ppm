from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid
from Products.validation.config import validation
try:
    from Products.validation.interfaces.IValidator import IValidator
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
    from interfaces.IValidator import IValidator
    del sys, os

from cenditel.ppm import CenditelPpmMF as _

ValidatorsList=[]

class GroupsValidator:
    """
       Validator for empty fields are not in groups within
       the portfolio of projects
    """

    __implements__ = IValidator

    def __init__(self,
        name,
        title='Groups validator',
        description='You will fail'):
            self.name = name
            self.title = title or name
            self.description = description

    def __call__(self, value, *args, **kwargs):
    	  Dic=value[0]
    	  value = str(value)
    	  if Dic['Title']=='':
    	      return _(u'Group required, please correct.')
       
ValidatorsList.append(GroupsValidator('isGroups', title='', description=''))

class UsersValidator:
    """
       Validator for empty fields are not in users within projects
    """

    __implements__ = IValidator

    def __init__(self,
        name,
        title='Users validator',
        description='Your users will fail'):
            self.name = name
            self.title = title or name
            self.description = description

    def __call__(self, value, *args, **kwargs):
    	  Dic=value[0]
    	  value = str(value)
    	  if Dic['Title']=='':
    	      return (_(u'A user required to select, please correct.'))
       
ValidatorsList.append(UsersValidator('areThereUsers', title='', description=''))

class SuscriberValidator:
	
    """
       Validator adress email
    """

    __implements__ = IValidator
    
    def __init__(self,
        name,
        title='Suscribers Validator',
        description='Your suscribers will fail'):
            self.name = name
            self.title = title or name
            self.description = description
       
    def __call__(self, value, *args, **kwargs):

        Wrongs=[]
        for email in value:
            
            try:
                checkEmailAddress(email)
            except EmailAddressInvalid:

                Wrongs.append(email)
        if len(Wrongs)==1:
            return _(u"The next email address is invalid: %s") % (Wrongs[0])
        elif len(Wrongs)>1:
            spanWrong=", ".join(Wrongs)
            return _(u"The nexts email addresses are invalid: %s ") % (spanWrong)
        else:
            pass

ValidatorsList.append(SuscriberValidator('areSuscribers', title='', description=''))

    

for validador in ValidatorsList:
         validation.register(validador)
         
         
         
    
