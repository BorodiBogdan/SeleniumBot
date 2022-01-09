from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

Chrome = webdriver.Chrome(executable_path="D:\web driver\chromedriver_win32\chromedriver.exe") #PBinfo
Firefox = webdriver.Firefox(executable_path="D:\geckodriver-v0.28.0-win64\geckodriver.exe") #SolInfo

PbInfo = "https://www.pbinfo.ro/" #unde imi fac eu veacul
SolInfo = "https://solinfo.ro/probleme"

UserName = "BandB"
PassWord = "parolanoua"

Chrome.get("https://solinfo.ro/solutie-noua")
Firefox.get(SolInfo)

def Login(Driver, username, parola):
    Driver.find_element_by_id("user").send_keys(username)
    Driver.find_element_by_id("parola").send_keys(parola)
    Driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    time.sleep(2)

def LoginSolInfo(Driver, username, password):
    time.sleep(2)
    email = Driver.find_elements_by_tag_name("input")
    email[1].send_keys(username)
    time.sleep(1)
    Click = Driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/button')
    Click.click()
    time.sleep(2)
    passw = Driver.find_element_by_id("password")
    passw.send_keys(password)
    time.sleep(2)
    Click2 = Driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/button')
    Click2.click()
    time.sleep(1)

def SolMea(Driver):
    Sol = Driver.find_element_by_css_selector("table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > label:nth-child(1) > kbd:nth-child(1)").text
    Sol = Sol.replace("#", "")
    NewUrl = "https://www.pbinfo.ro/detalii-evaluare/" + Sol
    Driver.get(NewUrl)

def CopyProblem(driver) :
    SolvedProblem = driver.find_element_by_tag_name("pre")
    SolvedProblem.send_keys(Keys.CONTROL, 'a')
    time.sleep(1)
    SolvedProblem.send_keys(Keys.CONTROL, 'c')

def WriteProblem(driver, problem) :
    message = driver.find_elements_by_tag_name("textarea")
    message[0].click()
    message[0].send_keys(Keys.CONTROL, 'v')
    time.sleep(1)
    input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/div/div/input')
    input.send_keys(problem)
    time.sleep(3.5)
    input.send_keys(Keys.DOWN)
    time.sleep(2)
    input.send_keys(Keys.ENTER)
    time.sleep(2)
    send = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[4]/button')
    send.click()
    time.sleep(2)
    print(problem)

def isproblem(driver) :
    if driver.title == "www.pbinfo.ro" :
        return 0
    else :
        return 1

time.sleep(3)
LoginSolInfo(Chrome, "bogdanborodiv@gmail.com", "PB1nf024")

Chrome.get(PbInfo)
Login(Chrome, UserName, PassWord)

time.sleep(2)

Click = Firefox.find_elements_by_class_name("MuiDataGrid-columnHeaderTitle")[3];
Click.click()

time.sleep(2)

Next = Firefox.find_elements_by_tag_name("button")

time.sleep(2)

c = 0

for index in Next:
    index.location_once_scrolled_into_view
    c += 1

cnt = 0

unsolved = []
path = "/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div/div/div[2]/div[2]/div/div/div/div/div/div["
s = "]/div[1]"

search = Chrome.find_element_by_id("search_box")
lupa = Chrome.find_elements_by_class_name("input-group-btn")

cc = 0

for index in range(24, 1052):
    aa = index % 50

    if(aa == 0):
        aa = 50
    p = path + str(aa) + s
    Problems = Firefox.find_elements_by_xpath(p)
    Sol = Problems[0].text
    NewUrl = "https://www.pbinfo.ro/?pagina=solutie-oficiala&id=" + Sol
    Chrome.get(NewUrl)
    pre = Chrome.find_elements_by_tag_name('pre')
    if(len(pre) > 0):
        time.sleep(3)
        Add = "https://solinfo.ro/solutie-noua"
        CopyProblem(Chrome)
        time.sleep(2.5)
        Chrome.get(Add)
        time.sleep(4.5)
        WriteProblem(Chrome, Sol)
        time.sleep(2)
        cc += 1
        print index

    if index % 50 == 0:
        Next[c - 4].click()
        time.sleep(2)

    if(cc >= 230):
        break

time.sleep(2)
print cc
