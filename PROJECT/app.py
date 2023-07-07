from flask import Flask, render_template, request
from flask_cors import cross_origin
from aima.logic import *
from aima.utils import *



app = Flask(__name__)



System = [
    "Windows",
    "Linux",
    "MacOS"
]

Category = [
    "TextEditor",
    "ProjectManagement",
    "ComptLog",
    "SecurityLog",
    "Design",
    "RelationClient",
    "DevLog",
    "Conference",
]

Price = [
    "Gratuit",
    "Payant"
]



def recommendation_system(facts):

    fc = FolKB()
    pc = PropKB()

    regles = []


#   GratuitWindows
    textEditGratuitWindows = ["Abiword", "Google_Docs", "Liber_Office_Writer", "Open_Office_Writer", "Free_Office_Text_Maker","DropBox_Paper"]
    projectManagementGratuitWindows = ["Trello", "Asana", "Wrike", "Team_Work"," ClickUp", "Zoho_Projects", "TeamGantt", "Basecamp", "Gouti","Sciforma ","VisualProjet","FoxPlan","Smartsheet","Wimi","Microsoft_Project","Jira","Podio" ,"Freedcamp,Notion"]
    ComptLogGratuitWindows = ["Sage" ,"Tiime","Pennylane","Freshbooks" ,"Zefyr","Itool","Axonaut"]
    SecurityLogGratuitWindows = ["McAfee",  "Norton"," Kaspersky", "Avira"," Microsoft_Defender", "Avast", "BullGuard","AVG","Adaware","Bitdefender","Intego"]
    designGratuitWindows = ["Figma","CorelDRAW" ,"Gimp","Canva","Crello","Drawio","Inkscape"]
    relationClientGratuitWindows = ["Zoho_CRM","Blue_Note_Systems_CRM","Simple_CRM","Webmecanik_Pipeline_CRM"]
    devLogGratuitWindows = [ "Visual_Studio", "Eclipse","HTML_Editor", "IntellijIdea"," PHP_Storm", "Atom", "Kiuwan","Komodo", " Hippo_CMMS", "Notepad","CodeScene","Code_Blocks","Apache_Netbrains"]
    conferenceGratuitWindows = ["Zoom","Microsoft_Teams", "Zoho_Meeting","KMeet", "Google_Meet","Skype"," Whereby","LiveStorm","Jitsi","TeamViewer","Webx"]

    for item in textEditGratuitWindows:
        regles.append(f"System(Windows) & Price(Gratuit) & Category(TextEditor) ==> Logiciel({item})")

    for item in projectManagementGratuitWindows:
        regles.append(f"System(Windows) & Price(Gratuit) & Category(ProjectMAnagement) ==> Logiciel({item})")

    for item in ComptLogGratuitWindows:
        regles.append(f"System(Windows) & Price(Gratuit) & Category(ComptLog) ==> Logiciel({item})")

    for item in SecurityLogGratuitWindows:
        regles.append(f"System(Windows) & Price(Gratuit) & Category(SecurityLog) ==> Logiciel({item})")

    for item in designGratuitWindows:
        regles.append(f"System(Windows) & Price(Gratuit) & Category(Design) ==> Logiciel({item})")

    for item in relationClientGratuitWindows:
        regles.append(f"System(Windows) & Price(Gratuit) & Category(RelationClient) ==> Logiciel({item})")

    for item in devLogGratuitWindows:
        regles.append(f"System(Windows) & Price(Gratuit) & Category(DevLog) ==> Logiciel({item})")

    for item in conferenceGratuitWindows:
        regles.append(f"System(Windows) & Price(Gratuit) & Category(Conference) ==> Logiciel({item})")



#  PayantWindows
    textEditorPayantWindows = ["Microsof_Word", "WPS_Ofiice_Writer","Zoho_Writer"]
    projectManagementPayantWindows = ["Asana"," Monday"," Team_Work"," ClickUp","TeamGantt","Gouti","Sciforma ","VisualProjet","FoxPlan","Smartsheet" ,"Jira" ,"Podio" ,"Notion"]
    ComptLogPayantWindows = ["QuickBooks"," Sage" ,"Tiime","Je_Pilote_Mon_Entreprise"," Indy,Pennylane","Sage_50_Comptabilite" ,"Freshbooks","MaComptafr ","Zefyr","Itool","Axonaut","Shine","Evoliz"]
    SecurityLogPayantWindows = ["BullGuard", "Intego"]
    DesignPAyantWindows = ["Adobe_Photoshop", "Adobe_Illustrator","Adobe_XD"," Adobe_After_Effects","Adobe_InDesign","CorelDRAW","Canva","Sketch","Pixen"]
    RelationClientPayantWindows = ["Salesforce","HubSpot","Suite_CRM_Sellsy","Talkspirit","Blue_Note_Systems_CRM","RingCentral","Teamleader"]
    DevLogPayantWindows = ["Intellij_Idea","HTML_Editor","PHP_Storm","Atom,Kiuwan","Hippo_CMMS","CodeScene"]
    ConferencePayantWindows = ["Zoom","Whereby" ,"LiveStorm"]

    for item in textEditorPayantWindows:
        regles.append(f"System(Windows) & Price(Payant) & Category(TextEditor) ==> Logiciel({item})")

    for item in projectManagementPayantWindows:
        regles.append(f"System(Windows) & Price(Payant) & Category(ProjectMAnagement) ==> Logiciel({item})")

    for item in ComptLogPayantWindows:
        regles.append(f"System(Windows) & Price(Payant) & Category(ComptLog) ==> Logiciel({item})")

    for item in SecurityLogPayantWindows:
        regles.append(f"System(Windows) & Price(Payant) & Category(SecurityLog) ==> Logiciel({item})")

    for item in DesignPAyantWindows:
        regles.append(f"System(Windows) & Price(Payant) & Category(Design) ==> Logiciel({item})")

    for item in RelationClientPayantWindows:
        regles.append(f"System(Windows) & Price(Payant) & Category(RelationClient) ==> Logiciel({item})")

    for item in DevLogPayantWindows:
        regles.append(f"System(Windows) & Price(Payant) & Category(DevLog) ==> Logiciel({item})")

    for item in ConferencePayantWindows:
        regles.append(f"System(Windows) & Price(Payant) & Category(Conference) ==> Logiciel({item})")



    # GratuitLinux
    textEditGratuitLinux = ["Abiword", "Google_Docs", "Liber_Office_Writer","Vim","Open_Office_Writer", "Free_Office_Text_Maker","DropBox_Paper","Emacs"]
    projectManagementGratuitLinux = ["Trello","Asana","Wrike","Team_Work","ClickUp","Zoho_Projects","TeamGantt","Basecamp","VisualProjet","FoxPlan","Smartsheet","Wimi","Jira","Podio" ,"Freedcamp,Notion"]
    ComptLogGratuitLinux = ["Sage","Crossover_Linux","Tiime","Freshbooks","Wine","Zefyr","Axonaut"]
    SecurityLogGratuitLinux = ["McAfee","Norton","Kaspersky", "Avira","AVG","Adaware","Intego"]
    designGratuitLinux = ["Figma","CorelDRAW" ,"Gimp","Canva","Crello","Lucidchart","Inkscape"]
    relationClientGratuitLinux = ["Vtiger","Fat_Free_CRM","Zoho_CRM","HubSpot","Simple_CRM","PipeDrive","Nimble","Apptivo_CRM"]
    devLogGratuitLinux = ["Visual_Studio","Eclipse","IntellijIdea","Atom","Kiuwan","Komodo","Hippo_CMMS","Notepad","CodeScene","Code_Blocks","Apache_Netbrains"]
    conferenceGratuitLinux = ["Zoom", "Zoho_Meeting","KMeet", "Google_Meet","Skype","LiveStorm","Jitsi","TeamViewer","Webx"]

    for item in textEditGratuitLinux:
        regles.append(f"System(Linux) & Price(Gratuit) & Category(TextEditor) ==> Logiciel({item})")

    for item in projectManagementGratuitLinux:
        regles.append(f"System(Linux) & Price(Gratuit) & Category(ProjectMAnagement) ==> Logiciel({item})")

    for item in ComptLogGratuitLinux:
        regles.append(f"System(Linux) & Price(Gratuit) & Category(ComptLog) ==> Logiciel({item})")

    for item in SecurityLogGratuitLinux:
        regles.append(f"System(Linux) & Price(Gratuit) & Category(SecurityLog) ==> Logiciel({item})")

    for item in designGratuitLinux:
        regles.append(f"System(Linux) & Price(Gratuit) & Category(Design) ==> Logiciel({item})")

    for item in relationClientGratuitLinux:
        regles.append(f"System(Linux) & Price(Gratuit) & Category(RelationClient) ==> Logiciel({item})")

    for item in devLogGratuitLinux:
        regles.append(f"System(Linux) & Price(Gratuit) & Category(DevLog) ==> Logiciel({item})")

    for item in conferenceGratuitLinux:
        regles.append(f"System(Linux) & Price(Gratuit) & Category(Conference) ==> Logiciel({item})")


# PayantLinux
    textEditorPayantLinux = ["WPS_Ofiice_Writer","Zoho_Writer","UltraEdit","Kojo","CLion","DataGrip"]
    projectManagementPayantLinux = ["Asana"," Monday"," Team_Work"," ClickUp","TeamGantt","Gouti","Sciforma ","VisualProjet","FoxPlan","Smartsheet" ,"Jira" ,"Podio" ,"Notion"]
    ComptLogPayantLinux = ["QuickBooks"," Sage" ,"Tiime","Je_Pilote_Mon_Entreprise","Sage_50_Comptabilite" ,"MaComptafr ","Zefyr","Itool","Axonaut","Shine","Evoliz"]
    SecurityLogPayantLinux = ["BullGuard","Intego","Nessus_Professional","Tenable_io","Snort","Suricata","Core_impact","Acunetix","Security_onion"]
    DesignPAyantLinux = ["CorelDRAW","Canva","Sketch","Pixen"]
    RelationClientPayantLinux = ["Salesforce","HubSpot","Suite_CRM_Sellsy","Talkspirit","Blue_Note_Systems_CRM","RingCentral","Teamleader"]
    DevLogPayantLinux = ["Intellij_Idea","HTML_Editor","PHP_Storm","Atom,Kiuwan","Hippo_CMMS","CodeScene"]
    ConferencePayantLinux = ["Zoom","Whereby" ,"LiveStorm"]

    for item in textEditorPayantLinux:
        regles.append(f"System(Linux) & Price(Payant) & Category(TextEditor) ==> Logiciel({item})")

    for item in projectManagementPayantLinux:
        regles.append(f"System(Linux) & Price(Payant) & Category(ProjectMAnagement) ==> Logiciel({item})")

    for item in ComptLogPayantLinux:
        regles.append(f"System(Linux) & Price(Payant) & Category(ComptLog) ==> Logiciel({item})")

    for item in SecurityLogPayantLinux:
        regles.append(f"System(Linux) & Price(Payant) & Category(SecurityLog) ==> Logiciel({item})")

    for item in DesignPAyantLinux:
        regles.append(f"System(Linux) & Price(Payant) & Category(Design) ==> Logiciel({item})")

    for item in RelationClientPayantLinux:
        regles.append(f"System(Linux) & Price(Payant) & Category(RelationClient) ==> Logiciel({item})")

    for item in DevLogPayantLinux:
        regles.append(f"System(Linux) & Price(Payant) & Category(DevLog) ==> Logiciel({item})")

    for item in ConferencePayantLinux:
        regles.append(f"System(Linux) & Price(Payant) & Category(Conference) ==> Logiciel({item})")




#  GratuitMacOS
    textEditGratuitMacOS = ["Abiword", "Google_Docs", "Liber_Office_Writer", "Open_Office_Writer", "Free_Office_Text_Maker","DropBox_Paper"]
    projectManagementGratuitMacOS = ["Trello", "Asana", "Wrike", "Team_Work"," ClickUp", "Zoho_Projects", "TeamGantt", "Basecamp", "Gouti","Sciforma ","VisualProjet","FoxPlan","Smartsheet","Wimi","Jira","Podio" ,"Freedcamp,Notion"]
    ComptLogGratuitMacOS = ["Sage" ,"Tiime","Pennylane","Freshbooks" ,"Zefyr","Itool","Axonaut"]
    SecurityLogGratuitMacOS = ["McAfee",  "Norton"," Kaspersky", "Avira", "Avast", "BullGuard","AVG","Adaware","Bitdefender","Intego"]
    designGratuitMacOS = ["Figma","CorelDRAW" ,"Gimp","Canva","Crello","Drawio","Inkscape"]
    relationClientGratuitMacOS = ["Zoho_CRM","Blue_Note_Systems_CRM","Simple_CRM","Webmecanik_Pipeline_CRM"]
    devLogGratuitMacOS = [ "Visual_Studio", "Eclipse","HTML_Editor", "IntellijIdea"," PHP_Storm", "Atom", "Kiuwan","Komodo", " Hippo_CMMS", "Notepad","CodeScene","Code_Blocks","Apache_Netbrains"]
    conferenceGratuitMacOS = ["Zoom", "Zoho_Meeting","KMeet", "Google_Meet","Skype"," Whereby","LiveStorm","Jitsi","TeamViewer","Webx"]

    for item in textEditGratuitMacOS:
        regles.append(f"System(MacOS) & Price(Gratuit) & Category(TextEditor) ==> Logiciel({item})")

    for item in projectManagementGratuitMacOS:
        regles.append(f"System(MacOS) & Price(Gratuit) & Category(ProjectMAnagement) ==> Logiciel({item})")

    for item in ComptLogGratuitMacOS:
        regles.append(f"System(MacOS) & Price(Gratuit) & Category(ComptLog) ==> Logiciel({item})")

    for item in SecurityLogGratuitMacOS:
        regles.append(f"System(MacOS) & Price(Gratuit) & Category(SecurityLog) ==> Logiciel({item})")

    for item in designGratuitMacOS:
        regles.append(f"System(MacOS) & Price(Gratuit) & Category(Design) ==> Logiciel({item})")

    for item in relationClientGratuitMacOS:
        regles.append(f"System(MacOS) & Price(Gratuit) & Category(RelationClient) ==> Logiciel({item})")

    for item in devLogGratuitMacOS:
        regles.append(f"System(MacOS) & Price(Gratuit) & Category(DevLog) ==> Logiciel({item})")

    for item in conferenceGratuitMacOS:
        regles.append(f"System(MacOS) & Price(Gratuit) & Category(Conference) ==> Logiciel({item})")




    #  PayantMacOS
    textEditorPayantMacOS = ["Microsof_Word", "WPS_Ofiice_Writer","Zoho_Writer"]
    projectManagementPayantMacOS = ["Asana"," Monday"," Team_Work"," ClickUp","TeamGantt","Gouti","Sciforma ","VisualProjet","FoxPlan","Smartsheet" ,"Jira" ,"Podio" ,"Notion"]
    ComptLogPayantMacOS = ["QuickBooks"," Sage" ,"Tiime","Je_Pilote_Mon_Entreprise"," Indy,Pennylane","Sage_50_Comptabilite" ,"Freshbooks","MaComptafr ","Zefyr","Itool","Axonaut","Shine","Evoliz"]
    SecurityLogPayantMacOS = ["BullGuard", "Intego"]
    DesignPAyantMacOS = ["Adobe_Photoshop", "Adobe_Illustrator","Adobe_XD"," Adobe_After_Effects","Adobe_InDesign","CorelDRAW","Canva","Sketch","Pixen"]
    RelationClientPayantMacOS = ["DayLite","FreshSales","Salesforce","HubSpot","Suite_CRM_Sellsy","Talkspirit","Blue_Note_Systems_CRM","RingCentral","Teamleader"]
    DevLogPayantMacOS = ["XCode","Visual_Studio_For_Mac","RubyMine","Intellij_Idea","HTML_Editor","PHP_Storm","Atom,Kiuwan","Hippo_CMMS","CodeScene"]
    ConferencePayantMacOS = ["GoTOMeeting","Skype_For_business","Blue_Jeans","Cisco_Jabber","Adobe_Connect","Join_Me","Fuze","Zoom","Whereby" ,"LiveStorm"]

    for item in textEditorPayantMacOS:
        regles.append(f"System(MacOS) & Price(Payant) & Category(TextEditor) ==> Logiciel({item})")

    for item in projectManagementPayantMacOS:
        regles.append(f"System(MacOS) & Price(Payant) & Category(ProjectMAnagement) ==> Logiciel({item})")

    for item in ComptLogPayantMacOS:
        regles.append(f"System(MacOS) & Price(Payant) & Category(ComptLog) ==> Logiciel({item})")

    for item in SecurityLogPayantMacOS:
        regles.append(f"System(MacOS) & Price(Payant) & Category(SecurityLog) ==> Logiciel({item})")

    for item in DesignPAyantMacOS:
        regles.append(f"System(MacOS) & Price(Payant) & Category(Design) ==> Logiciel({item})")

    for item in RelationClientPayantMacOS:
        regles.append(f"System(MacOS) & Price(Payant) & Category(RelationClient) ==> Logiciel({item})")

    for item in DevLogPayantMacOS:
        regles.append(f"System(MacOS) & Price(Payant) & Category(DevLog) ==> Logiciel({item})")

    for item in ConferencePayantMacOS:
        regles.append(f"System(MacOS) & Price(Payant) & Category(Conference) ==> Logiciel({item})")



    #   we fill the knowledge base 
    for rule in regles:
        fc.tell(expr(rule))


    for fact in facts:
        fc.tell(expr(fact))

    result = list(fol_fc_ask(fc,expr("Logiciel(y)")))

    return result

app.config['ENV'] = 'development'
app.config['Debug'] = True
app.config['TESTING'] = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tictactoe-game')
def tictactoe():
    return render_template('TicTacToe.html')


@app.route('/expert-system', methods=['GET', 'POST'])
def expertsystem():
    if request.method == 'POST':
        username = request.form['username']
        operatingSystem = request.form['operatingSystem']
        softwareType = request.form['softwareType']
        softwarePrice = request.form['softwarePrice']
        list = {
            'username': username,
            'operatingSystem': operatingSystem,
            'softwareType': softwareType,
            'softwarePrice': softwarePrice,
        }
        print('username: ', username)
        print('operatingSystem: ', operatingSystem)
        print('softwareType: ', softwareType)
        print('softwarePrice: ', softwarePrice)
        if not username:
            error = 'Username is required.'
        if not operatingSystem:
            error = 'operatingSystem is required.'
        elif not softwareType:
            error = 'softwareType is required.'
        elif not softwarePrice:
            error = 'softwarePrice is required.'
            return render_template('ExpertSystem.html', error=error)
        data = recommendation_system([f"System({operatingSystem})",f"Price({softwarePrice})",f"Category({softwareType})"])

        results = []
        for dt in data :
            # print(dt)
            results.append(dt[y])
        print(results)
        # return render_template('ExpertSystem.html', list=list)
        return render_template('ExpertSystem.html', list=list, results=results, System=System, Category=Category, Price=Price)
    return render_template('ExpertSystem.html')
    


if __name__ == '__main__':
    app.run()