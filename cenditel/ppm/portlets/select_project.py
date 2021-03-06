from Acquisition import aq_parent

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope.formlib import form
from zope.interface import implements

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from cenditel.ppm import searchportlet
from cenditel.ppm import CenditelPpmMF as _

class IProjectsDashboardPortlet(IPortletDataProvider):
    pass

class Assignment(base.Assignment):
    implements(IProjectsDashboardPortlet)

    @property
    def title(self):
        return _(u"Projects Dashboard")

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('select_project.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)
        
    def title (self):
        return "hola"

    def searching(self):
        z=searchportlet.searching()
        self.result=z.searching(self.context)
        return self.result        
        
    def GetTags(self):
        """
        the tag list that are within the portfolio of projects
        """
        tagsList=[]
    	for element in self.result:
    	    tagsList.extend(element.getTags())
        return tagsList
        
    def GetManagers(self):
        Manag=[]
        NewListManag=[]
        for NM in self.result:
            managerobject= NM.getManager()
            Manag.extend(managerobject)
            
        for x in Manag:
            if not x in NewListManag:
                NewListManag.append(x)
            else:
                pass
        return NewListManag 

        
    def gosearch(self):
        holder=self.context
        if self.request.form.has_key('form.button.Search'):
            C_url=holder.absolute_url()
            Urls= C_url + "/@@SearchPro"
            manager=self.request.form["manager"]
            tag=self.request.form["tag"]
            import pdb; pdb.set_trace()
            return self.request.RESPONSE.redirect(Urls)
            
    
"""        
    def title (self):
        list=[]
        holder=self.context
        for child in holder.getChildNodes(): 
            list.append({child.Title():child.absolute_url()})
        return list

    @property
    def getMemberProfile(self):
        
        
        text = profile.text()
        parms = {}
        for line in text.split('\n'):
            if line.startswith('#'):              # Comment line
                continue
            elif line.startswith('Application:'): # Application Identifier
                (x, app) = line.split(':')
                app = app.strip()
            elif line.find(':') > -1:             # Parameter value
                if app in ('All', 'Projects'):
                    (var, val) = line.split(':')
                    val = val.strip()
                    if val.startswith('[') or val.startswith('('):
                        for x in ('[]()\'"'):
                            val = val.replace(x,'')
                        (lst) = val.split(',')
                        parms[var] = lst
                    else:
                        parms[var] = val.strip()
        return parms
        
        if mbr == 'Anonymous User':
            return {}
        
        try:
            profiles = getattr(context, 'profiles')
        except:
            return {}
        
        mbr = mbr.title()
        
        if hasattr(profiles, mbr):
            profile = getattr(profiles, mbr)
            return getMbrProfile(profile)
        else:
            return {}

    @property
    def getPPMUrl(self):
      
        
        folder = context
          
        while 1:
            try:
                if folder.portal_type == 'PPM':
                    break
            except:
                return context.absolute_url()
        try:
            folder = folder.aq_parent
            continue
        except:
            return context.absolute_url()
        
        return folder.absolute_url()

    @property
    def getFormTags(self):
       
        
        request = container.REQUEST
        
        if key in ('tag', 'xtag'):
            dict = {}
            for val in parms[key]:
                dict[val]=1
            return dict
        else:
            return parms[key]
        
        if request.form.has_key(key):
            data = request.form[key]
            
            if data == '':
                if parms.has_key(key):
                    data = getparms(key)
            elif key in ('tag', 'xtag'):
                dict = {}
                if hasattr(data, 'startswith'): # data is string
                    dict[data] = 1
            else:
                for t in data:
                    dict[t] = 1
                rdata = dict
            else:
                rdata = data
            return rdata
        
        elif parms.has_key(key):
            return getparms(key)
        
        else:
            if key in ('tag', 'xtag'):
                return {}
            else:
                return ''
"""

class AddForm(base.NullAddForm):
    form_fields = form.Fields(IProjectsDashboardPortlet)
    label = _(u"Add Projects Portlet")
    description = _(u"This portlet displays a form for select some criteria and find quickly projects registered based on those criteria.")

    def create(self):
        return Assignment()


#class EditForm(base.EditForm):
#    form_fields = form.Fields(IProjectsDashboardPortlet)
#    label = _(u"Edit Projects Portlet")
#    description = _(u"This portlet displays a form for select some criteria and find quickly projects registered based on those criteria.")

