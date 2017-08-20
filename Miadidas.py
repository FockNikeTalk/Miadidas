import json, requests, time, random, re, thread, urllib3	
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

list1 = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]


url = 'https://brand.campaign.adidas.com/api/scv/subscription/newsletter/create'

headers = {
							'Origin'         : 'http://www.adidas.com',
							'Accept-Encoding': 'gzip, deflate, br',
							'Accept-Language': 'en-US,en;q=0.8',
							'User-Agent'     : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
							'Content-Type'   : 'application/json; charset=UTF-8',
							'Accept'         : 'application/json, text/javascript, */*; q=0.01',
							'Referer'        : 'http://www.adidas.com/us/mi_ultraboost',
							'Connection'     : 'keep-alive',
			}
class GmailDotEmailGenerator:
  def __init__(self, email):
    self.__username__, self.__domain__ = email.split('@')
  def generate(self):
    return self.__generate__(self.__username__, self.__domain__)
  def __generate__(self, username, domain):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@" + domain)
    return emails

def miadidas(emails):
    for email in \
            (GmailDotEmailGenerator(emails).generate())[:1000000]:
		payload ={
 				"email"        		: email, # Do Not change
				"firstName"    		: list1[random.randint(0, 99)], # Do Not change
				"lastName"      	: list1[random.randint(0, 99)], # Do Not change
				"gender"        	: "M", # Do Not change
				"datepicker"    	: "9/15/1993", # Do Not change
				"dateOfBirth"   	: "1993-09-15", # Do Not change
				"countryOfSite" 	: "US", # Do Not change
				"newsletterDomain"  : "United States", # Do Not change
				"newsletterLanguage": "en",# Do Not change
				"newsletterTypeId"  : "40000", # Do Not change
				"source"            : "90891", # Do Not change
				"eventType"         : "0", # Do Not change
				"sendMail"          : "N", # Do Not change
				"consents"          : {"consent": [{"consentType": "AMF", "consentValue": "N", "consentVersion": "ADIUS_VER_1"}]} # Do Not change
			}
		payload = json.dumps(payload)
		resp = requests.post(url, verify=False, data=payload, headers=headers)
		if any(re.findall(r'true', str(resp.text), re.IGNORECASE)):
		            print(time.strftime("[%H:%M:%S]") + " - Succesfully entered" + " - " + email)
		else:
		           print(time.strftime("[%H:%M:%S]") + " - Could not enter" + " - " + resp.text)
try:
   thread.start_new_thread( miadidas, ("youremail@gmail.com",) ) # Change to your email
   thread.start_new_thread( miadidas, ("youremail@gmail.com",) ) # add another mail if u want, delete this line if not
   thread.start_new_thread( miadidas, ("youremail@gmail.com",) ) # add another mail if u want, delete this line if not

except:
    print "Error: unable to start thread"
while 1:
    pass
