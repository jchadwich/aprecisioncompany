from django.shortcuts import render
from models import Docgen



def docgen(request):
    if request.method == 'POST':
        # print("hey")

        inFile = request.POST['inFile']
        city = request.POST['city']
        state = request.POST['state']
        entity = request.POST['entity']
        outFileType = request.POST['outFileType']
        pricingType = request.POST['pricingType']
        conName = request.POST['conName']
        conTitle = request.POST['conTitle']
        conPH = request.POST['conPH']
        conAddress = request.POST['conAddress']
        conEmail = request.POST['conEmail']
        bdName = request.POST['bdName']
        bdTitle = request.POST['bdTitle']
        bdPH = request.POST['bdPH']
        bdExtension = request.POST['bdExtension']
        projName = request.POST['projName']
        pprNum = request.POST['pprNum']
        poNum = request.POST['poNum']
        specs = request.POST['specs']
        dnrCost = request.POST['dnrCost']
        smCost = request.POST['smCost']
        mdCost = request.POST['mdCost']
        lgCost = request.POST['lgCost']
        curbCost = request.POST['curbCost']
        segways = request.POST['segways']
        safetyIncidents = request.POST['safetyIncidents']
        knownDaysToFinish = request.POST['knownDaysToFinish']
        minDaysToFinish = request.POST['minDaysToFinish']
        maxDaysToFinish = request.POST['maxDaysToFinish']
        techs = request.POST['techs']
        pssMin = request.POST['pssMin']
        woLoc = request.POST['woLoc']
        mapData = request.POST['mapData']

        print(outFileType)

        dg = Docgen(inFile=inFile, city=city, state=state, entity=entity, outFileType=outFileType,
                    pricingType=pricingType, conName=conName, conTitle=conTitle, conPH=conPH,
                    conAddress=conAddress, conEmail=conEmail, bdName=bdName, bdTitle=bdTitle,
                    bdPH=bdPH, bdExtension=bdExtension, projName=projName, pprNum=pprNum, poNum=poNum,
                    specs=specs, dnrCost=dnrCost, smCost=smCost, mdCost=mdCost, lgCost=lgCost, curbCost=curbCost,
                    segways=segways, safetyIncidents=safetyIncidents, knownDaysToFinish=knownDaysToFinish,
                    minDaysToFinish=minDaysToFinish, maxDaysToFinish=maxDaysToFinish, techs=techs,
                    pssMin=pssMin, woLoc=woLoc, mapData=mapData)

        dg.save()

    return render(request, 'docgen/docgen.html')

    # Map only
    # if outFileType == 1:
    #     from .map import Map
    #     Map()
    # # Pricing Sheet
    # elif outFileType == 3:
    #     from .pricingSheet import PricingSheetMap
    #     from .pricingSheet import Invoice
    #     PricingSheetMap()
    #     Invoice()
    # elif outFileType == 4:
    #     from .inftPpr import Doc
    #     Doc()
    # else:
    #     return

    # PPR
    # Doc()
