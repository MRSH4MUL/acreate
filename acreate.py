import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
def clear():
    os.system('clear')
    print(logo)
#-------------------[LOGO]-------------------#
logo='''\033[1;32m
 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣸⠀⣠⣄⡀⠀⣀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢨⣿⣿⣿⣿⣿⠀⠀⢀⡰⠡⣾⣿⣿⡇⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣸⣿⣿⣿⣿⣿⣆⠘⣥⣄⠀⠘⠋⠉⣴⣶⠉⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⡯⡿⢿⣿⣿⣿⣿⣿⣦⣯⠉⢹⣿⡆⠀⠉⠉⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡔⢸⣁⡇⢸⢸⣿⣿⣿⣿⣿⣿⠀⠀⠻⠿⠿⠷⠷⣿⣿⣿⣿⣿⣿⣿⡿⡛⠿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢣⣸⢸⢇⡏⣸⣿⣿⣿⣿⣿⣿⣿⠶⠤⠤⣄⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣉⠲⢮⢿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢿⣟⣿⣼⣿⣿⣿⣿⣿⣿⣿⠯⠭⠥⢦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢉⣿⠀⠈⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⡟⠚⡿⠿⣿⣿⣿⡿⣻⣿⠥⣤⣶⡶⢿⣭⣛⢿⣿⣿⣿⣿⣿⣿⣷⣶⡏⠀⣆⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⠀⡾⣷⠖⠒⡖⢿⣿⡿⠟⠛⠛⣉⡟⠛⠙⢯⠽⢿⣞⠙⡟⠛⠚⢿⣿⡿⠲⠿⢻⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⠀⢸⢀⡞⣷⣈⠻⢿⣶⣶⣶⣾⣷⣄⠀⣼⣷⣿⡿⣿⢧⡀⠀⣼⣿⣷⣄⠀⢸⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢠⡏⣸⣷⡘⠿⣷⣶⣤⣤⣤⣤⡴⢿⡄⠘⣿⣿⣶⡿⢆⣳⡄⠘⣿⣿⡇⢱⣾⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⢰⣾⣷⣿⡙⢿⣶⣤⣈⣉⣉⣉⣡⣴⣾⣄⠀⢹⣶⣭⣥⣿⢿⣿⣆⠈⢿⣇⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣯⠳⣤⡉⠛⠻⠿⠿⠿⠿⠛⣡⣿⡀⠘⣮⣙⣛⣋⣼⣿⣿⣦⣠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⠛⠷⣶⣤⣤⣴⣶⠿⠛⣡⡇⠘⣮⡻⢿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣀⣤⣴⣾⣿⣿⣶⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                 ⣿⣿⣿⣿⣿⣿⣿⣿⣿ BY WITH MR SH4MUL ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
————————————————————————————————————————————————————————————————————————————————————————————————————
'''

#-------------------[LINE]-------------------#
def __line__():
    print(f'\033[1;37m——————————————————————————————————————————————————\033[1;37m')    
infinix = random.choice(['7060', '8076D', 'F98', 'G636', 'GT 10 Pro', 'Hot', 'Hot 1', 'Hot 10', 'Hot 10 Play', 'Hot 10i', 'Hot 10s', 'Hot 10s NFC', 'Hot 10T', 'Hot 11', 'Hot 11 (2020)', 'Hot 11S', 'Hot 12', 'Hot 12 Play', 'Hot 12 Play NFC', 'Hot 12 Pro', 'Hot 12i', 'Hot 2', 'Hot 20',
    'Hot 20 5G', 'Hot 20 Play', 'Hot 20i', 'Hot 20S', 'Hot 3', 'Hot 3 Pro', 'Hot 30', 'Hot 30 Play', 'Hot 30i', 'Hot 4', 'Hot 4 Lite', 'Hot 4 Pro', 'Hot 5', 'Hot 5 Lite', 'Hot 6', 'Hot 6 Pro', 'Hot 6X', 'Hot 7', 'Hot 7 Pro', 'Hot 8', 'Hot 9', 'Hot 9 Play', 'Hot 9 Pro',
    'Hot Note', 'Hot S', 'Hot S3', 'Hot S3X', 'Hot V3', 'HOT4 LTE', 'HOT6 Pro', 'NOTE', 'Note 10', 'Note 10 Pro', 'Note 11', 'Note 11 Pro', 'Note 11S', 'Note 12', 'Note 12 (2023)', 'Note 12 NFC', 'Note 12 Pro', 'Note 12 Pro 5G', 'Note 12 VIP', 'Note 12i', 'Note 12i 2022',
    'Note 2', 'NOTE 2 LTE', 'Note 3', 'NOTE 3 Pro', 'Note 30 Pro', 'Note 30 VIP', 'Note 30i', 'Note 4', 'Note 4 Pro', 'Note 5', 'Note 5 Stylus', 'Note 6', 'Note 7', 'Note 7 Lite', 'Note 8', 'Note 8i', 'Race Bolt', 'Race Jet', 'Race Lite', 'S2', 'S2 Pro', 'S4', 'S5',
    'S5 Lite', 'S5 Pro', 'Smart 2', 'Smart 2 HD', 'Smart 2 Pro', 'Smart 3', 'Smart 3 Plus', 'Smart 4', 'Smart 4 Plus', 'Smart 5', 'Smart 6','Smart 6 HD', 'Smart 6 Plus', 'Smart 7', 'Smart 7 HD', 'Smart 7 Plus', 'Smart HD (2021)', 'Surf Bravo', 'Surf Noir', 'Surf Smart 2', 'Surf Smart 3G', 'X1000', 'X530', 'X6711', 'X6731', 'X678', 'X689', 'Y88', 'Zero', 'Zero 2', 'Zero 20', 'Zero 3', 'Zero 30', 'Zero 30 5G',
    'Zero 4', 'Zero 4 Plus', 'Zero 5', 'Zero 5G', 'Zero 6', 'Zero 6 Pro', 'Zero 8', 'Zero 8i', 'Zero Ultra', 'Zero X', 'Zero X Neo', 'Zero X Pro'])        
boy = [
    "Shanto Hasan",
    "Arif Hossain",
    "Rajib Ahmed",
    "Shakib Al Hasan",
    "Tanvir Rahman",
    "Rifat Chowdhury",
    "Samir Khan",
    "Naimul Islam",
    "Sohel Rana",
    "Farhan Ahmed",
    "Suman Das",
    "Rubel Hossain",
    "Anik Miah",
    "Shahin Alam",
    "Rony Sarker",
    "Tareq Ahmed",
    "Sadiq Hasan",
    "Rashedul Islam",
    "Jamil Hossain",
    "Saifur Rahman",
    "Asif Ali",
    "Shuvo Roy",
    "Nizam Uddin",
    "Muntasir Khan",
    "Hasan Mahmud",
    "Abir Chowdhury",
    "Fahim Hasan",
    "Rayan Sardar",
    "Shadman Islam",
    "Imran Ali",
    "Billal Hossain",
    "Nasim Uddin",
    "Shamsul Islam",
    "Anwar Hossain",
    "Emon Sarker",
    "Sadiq Rahman",
    "Rifat Hasan",
    "Shafiqul Islam",
    "Nayan Ahmed",
    "Jahid Hasan",
    "Kadir Miah",
    "Kamal Hossain",
    "Rony Ahmed",
    "Mizanur Rahman",
    "Arman Sheikh",
    "Samiul Islam",
    "Shajedul Islam",
    "Rubaiyat Hossain",
    "Babu Miah",
    "Akash Ahmed",
    "Jashim Uddin",
    "Rashed Khan",
    "Rafiq Hossain",
    "Nabil Ahmed",
    "Ashik Rahman",
    "Shihab Uddin",
    "Sakib Chowdhury",
    "Shafaat Hossain",
    "Mostafa Kamal",
    "Rohan Ahmed",
    "Rumman Hossain",
    "Faruq Miah",
    "Limon Rahman",
    "Zubair Hasan",
    "Saimon Islam",
    "Adnan Chowdhury",
    "Joynal Abedin",
    "Iftikhar Hossain",
    "Saad Miah",
    "Rubel Ahmed",
    "Monirul Islam",
    "Parvez Hossain",
    "Ahsan Ali",
    "Shakib Sarker",
    "Mubin Hossain",
    "Jamilur Rahman",
    "Sujan Ahmed",
    "Riyad Uddin",
    "Tamim Chowdhury",
    "Firoz Hossain",
    "Shomoy Hasan",
    "Ayman Miah",
    "Mahfuzur Rahman",
    "Arifin Islam",
    "Anirban Das",
    "Shakil Ahmed",
    "Zishan Hossain",
    "Sagar Miah",
    "Alif Rahman",
    "Tushar Chowdhury",
    "Rafiul Hasan",
    "Mustafizur Rahman",
    "Naim Hossain",
    "Shahin Miah",
    "Ramin Ahmed",
    "Shovon Hossain",
    "Arafat Ali",
    "Yamin Rahman",
    "Ayan Uddin",
    "Subhan Ahmed",
    "Nusrat Jahan",
    "Sabina Yasmin",
    "Maya Datta",
    "Shabnur",
    "Tanjin Tisha",
    "Rupa Ganguly",
    "Jaya Ahsan",
    "Pori Moni",
    "Shaila Sabiha",
    "Bipasha Hayat",
    "Keya Muna",
    "Dilara Hafiz",
    "Sharmila Tagore",
    "Anjana Sultana",
    "Priyanka Bandyopadhyay",
    "Moushumi",
    "Rani Mukerji",
    "Nabila Nasrin",
    "Shahnaz Khushi",
    "Aditi Rahman",
    "Sushmita Anis",
    "Roshni Noor",
    "Taslima Nasrin",
    "Kaniz Gopy",
    "Faria Shahrin",
    "Mahira Khan",
    "Rukhsana Ahmed",
    "Riya Saha",
    "Shirin Akhter",
    "Mehazabien Chowdhury",
    "Shabnam Faria",
    "Rimi Islam",
    "Sofia Ahmed",
    "Shaon Sultana",
    "Nafisa Sultana",
    "Afsana Mimi",
    "Kabori Sarwar",
    "Shilpi Sharma",
    "Sultana Zaman",
    "Nusrat Jahan Islam",
    "Kiran Shah",
    "Nazia Hassan",
    "Rupsa Dey",
    "Jessia Islam",
    "Shabana Nasrin",
    "Shirin Akhtar",
    "Farhana Mili",
    "Tisha Ahmed",
    "Sumiya Sultana",
    "Ruma Ahmed",
    "Priya Kundu",
    "Rimi Naz",
    "Momena Tasnim",
    "Shakila Parveen",
    "Farah Faye",
    "Trina Sultana",
    "Kaniz Shabnam",
    "Nazia Hossain",
    "Afsana Rahman",
    "Lubaba Zaman",
    "Sharmin Sultana",
    "Alisha Ahmed",
    "Kazi Nasrin",
    "Sonia Rahman",
    "Shaila Afsana",
    "Priyanka Das",
    "Tania Rahman",
    "Umme Salma",
    "Sumi Rahman",
    "Roshni Sultana",
    "Akhi Sultana",
    "Sumiya Farhana",
    "Rezwana Chowdhury",
    "Anita Das",
    "Laboni Sultana",
    "Tanisha Akhter",
    "Rezwana Islam",
    "Pori Hossain",
    "Farhana Rahman",
    "Shathi Sultana",
    "Kanak Shabnam",
    "Tisha Islam",
    "Shazna Rahman",
    "Maisha Chowdhury",
    "Ruma Sultana",
    "Shahana Hossain",
    "Tabassum Binte",
    "Farzana Noor",
    "Nahidul Islam",
    "Sabina Khatun"]
ua= f"Mozilla/5.0 (Linux; Android 7.0; {infinix} Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randrange(80,105))+".0."+str(random.randrange(1000,5000))+"."+str(random.randrange(100,399))+" Mobile Safari/537.36"
ok = []
cp = []
class create:
    def __init__(self):
        self.loop = 0
        self.gender = []
    def start(self):
        clear()
        print ('[1] Facebook account auto create')
        gen = input('select: ')
        print (47*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        else:
            self.gender.append('boy')
        print("LIMIT = 1000-10000-100000")
        lim = int(input('limit: '))
        clear()
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'viewport-width': '980',
        }
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
        }
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f"\r\r\033[1;37m[Hammadi-AUTO] {self.loop}|\033[1;32m{str(len(ok))}\033[1;37m|\033[1;31m{str(len(cp))}"),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = random.choice(['arx123','arx###','arx@@@','arxarx123','@#@#@#','@@@###','arx@#21','876876','009988','778899','506070','arx123','arxarxarx','arx£$£$','arxarx','arx@#@#','57273200','57575753','##@@##@@','E7r9t8@Q#h%Hy+M','S012cot5544fie76ld89','P@ssw0rd','Scotfield01255447689','DiamBloSecu','iloveyou','i love all country','respect all country'])
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;33m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;33m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;32m[OK] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                    print(f'\r\033[1;32m=[🍪]={coki}')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
                
                
                
create().start()       