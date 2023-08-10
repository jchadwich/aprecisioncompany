from django.contrib import admin

from .models import Docgen

class DocgenAdmin(admin.ModelAdmin):
    list_display = ('inFile', 'city', 'state', 'entity', 'outFileType', 'pricingType', 'conName', 'conTitle',
                    'conPH', 'conAddress', 'conEmail', 'bdName', 'bdTitle', 'bdPH', 'bdExtension', 'projName',
                    'pprNum', 'poNum', 'specs', 'dnrCost', 'smCost', 'mdCost', 'lgCost', 'curbCost', 'segways',
                    'safetyIncidents', 'knownDaysToFinish', 'minDaysToFinish', 'maxDaysToFinish', 'techs',
                    'pssMin', 'woLoc', 'mapData')

admin.site.register(Docgen, DocgenAdmin)
