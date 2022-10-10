from django.http import request, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordSetView,PasswordChangeView
from django.urls import reverse_lazy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.models import Bids, Userdata
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

startTime = time.time()

# My views
def Scraper(request):
    options = Options()
    # # options.add_extension('extension_3_0_6_0.crx')
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    driver.get("https://bidplus.gem.gov.in/all-bids")
    # "DELHI","PANIPAT",
    # states = [ "Delhi","Faridabad", "Ghaziabad", "Gautam Buddha Nagar", "Noida", "Sonipat", "Gurgaon", "Panipat"]
    driver.maximize_window()
    states = [ "Delhi","Faridabad", "Ghaziabad", "Gautam Buddha Nagar","Noida","Sonipat", "Gurgaon", "Panipat"]
    driver.maximize_window()

    for state in states:
        from selenium.webdriver.common.action_chains import ActionChains
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/input"))).clear()
        button = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/input")
        # button = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div[2]/input")
        # button.clear()
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(button).click(button).perform()

        button.send_keys(state)

        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/span[2]/button").click()
        time.sleep(10)

        # getting thw numver od the last oage
        try:
            print("this is state: ", state)
            x = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[13]/a[6]").get_attribute("text")

            if x == "Next":
                x = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[13]/a[5]").get_attribute("text")

        except Exception:
            print("this is state: ", state)
            try:
                x = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[13]/a[4]").get_attribute("text")
            except NoSuchElementException:
                x = 1
        print(x)

        for k in range(0, int(x)):
            try:
                for i in range(0, 10):
                    # getting bid number
                    Bid_number = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[" + str(
                        i + 2) + "]/div[1]/p/a").get_attribute("text")
                    # getting pdf href
                    Pdf_link = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[" + str(
                        i + 2) + "]/div[1]/p/a").get_attribute("href")
                    print(Bid_number)
                    print(Pdf_link)

                    # Item Name
                    try:
                        Item = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[" + str(
                            i + 2) + "]/div[3]/div/div[1]/div[1]/a").get_attribute("data-content")
                    except Exception as NoSuchElementException:
                        Item = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[" + str(
                            i + 2) + "]/div[3]/div/div[1]/div[1]").text

                    print(Item)

                    ItemList = Item.split(";")

                    FinalItem = ItemList[0]
                    if "Items:" in FinalItem:
                        FinalItem = FinalItem.replace("Items:", "")

                    #       Department name
                    Department_name = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[" + str(
                        i + 2) + "]/div[3]/div/div[2]/div[2]").text
                    # Department_name=driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[2]/div[3]/div[3]/div/div[2]/div[2]").text
                    # print(Department_name)
                    Dname = Department_name.splitlines()
                    # print(Dname)
                    if "NA" in Dname:
                        if Dname[0] == "NA":
                            Department = Dname[1]
                        else:
                            Department = Dname[0]
                    else:
                        Department = Dname[0]

                    print(Department)
                    start_date_pre = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[" + str(
                        i + 2) + "]/div[3]/div/div[3]/div[1]/span").text
                    start_list = start_date_pre.split()

                    start_date = start_list[0]
                    start_time = start_list[1] + " " + start_list[2]

                    print('Start date :', start_date)

                    import datetime
                    start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y").strftime("%Y-%m-%d")
                    print("Start Date final :", start_date)

                    print('Start time :', start_time)

                    end_date_pre = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div[" + str(
                        i + 2) + "]/div[3]/div/div[3]/div[2]/span").text
                    # end_date_pre=driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[2]/div[3]/div[3]/div/div[3]/div[2]/span").text
                    end_list = end_date_pre.split()
                    End_date = end_list[0]
                    End_time = end_list[1] + " " + end_list[2]

                    print('End Date :', End_date)
                    print('End Time :', End_time)

                    import datetime

                    End_date = datetime.datetime.strptime(End_date, "%d-%m-%Y").strftime("%Y-%m-%d")
                    print("End Date final :", End_date)

                    # Open a file with access mode 'a'
                    file_object = open('bids.txt', 'a')
                    # Append 'hello' at the end of file
                    file_object.write(Bid_number)
                    file_object.write("\n")
                    # Close the file
                    file_object.close()

                    # sheetEntry(d1,Bid_number,DepartmentName,Address,without_item,myFinalStartDate,start_time[1],end_time[0],end_time[1],pdfHref,location)
                    driver.execute_script('''window.open("http://127.0.0.1:8000/insert/","_blank");''')
                    print(driver.window_handles)

                    window_after = driver.window_handles[1]
                    driver.switch_to.window(window_after)
                    try:
                        driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys(Bid_number)
                        print("line 1")
                    except Exception:
                        driver.refresh()
                        driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys(Bid_number)
                        print("line 1")

                    driver.find_element(By.XPATH, "/html/body/form/input[3]").send_keys(Department)
                    print("line 2")
                    driver.find_element(By.XPATH, "/html/body/form/input[4]").send_keys(state + ", India ")
                    driver.implicitly_wait(1)
                    print("line 3")
                    driver.find_element(By.XPATH, "/html/body/form/input[5]").clear()
                    driver.find_element(By.XPATH, "/html/body/form/input[5]").send_keys(FinalItem)
                    driver.implicitly_wait(1)
                    print("line 4")
                    driver.find_element(By.XPATH, "/html/body/form/input[6]").clear()
                    driver.find_element(By.XPATH, "/html/body/form/input[6]").send_keys(str(start_date))
                    print("line 5")
                    driver.find_element(By.XPATH, "/html/body/form/input[7]").clear()
                    driver.find_element(By.XPATH, "/html/body/form/input[7]").send_keys(start_time)
                    print("line 6")
                    driver.find_element(By.XPATH, "/html/body/form/input[8]").clear()
                    driver.find_element(By.XPATH, "/html/body/form/input[8]").send_keys(str(End_date))
                    print("line 7")
                    driver.find_element(By.XPATH, "/html/body/form/input[9]").send_keys(End_time)
                    print("line 8")
                    try:
                        driver.find_element(By.XPATH, "/html/body/form/input[10]").send_keys(Pdf_link)
                    except:
                        driver.find_element(By.XPATH, "/html/body/form/input[10]").send_keys("NA")
                    print("line 9")
                    driver.find_element(By.XPATH, "/html/body/form/input[11]").send_keys(state + ", India ")
                    print("line 10")
                    driver.find_element(By.XPATH, "/html/body/form/button").click()
                    # time.sleep(2)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                # click on Next link text
                driver.find_element(By.LINK_TEXT, "Next").click()
            except Exception as e:
                print(e)
                break

    print('The script took {0} second !'.format(time.time() - startTime))

    finalText='The script took {0} second !'.format(time.time() - startTime)

    return  HttpResponse(finalText)

def home(request):
    if request.method == 'POST':
        bid=request.POST.get('bid')
        dname=request.POST.get('dname')
        address=request.POST.get('address')
        services=request.POST.get('services')
        sdate=request.POST.get('sdate')
        stime=request.POST.get('stime')
        edate=request.POST.get('edate')
        etime=request.POST.get('etime')
        pdflink=request.POST.get('pdflink')
        location=request.POST.get('location')
        # new = Bids(Bid_number=bid,Department_Name=dname,Address=address,Services=services,Start_date=sdate,Start_time=stime,End_date=edate,End_time=etime,PdfLink=pdflink,Location=location)
        # new.save()
        if not Bids.objects.filter(Bid_number=bid).exists():
             obj, created = Bids.objects.get_or_create(Bid_number=bid,Department_Name=dname,Address=address,Services=services,Start_date=sdate,Start_time=stime,End_date=edate,End_time=etime,PdfLink=pdflink,Location=location)

    return HttpResponse("<p>value inserted successfully !!!</p>")


def save_tender_settings(request):
    if request.method == 'POST':
        all=request.POST.get('all')
        current_user = request.user
        username=None
        if request.user.is_authenticated:
            username = request.user.username
        if not Userdata.objects.filter(User=username).exists():
             obj,created=Userdata.objects.get_or_create(User=username,Services=all)
        else:
            t = Userdata.objects.get(User=username)
            t.Services = all  # change field
            t.save()

        print(all)

    return HttpResponse("page working correctly :",all)


def tender_settings(request):
      return render(request,'tender-setup.html')

def search_address(request):
    address=request.GET.get("address")
    payload=[]
    if address:
        fake_address_objs=Bids.objects.filter(Services__icontains=address).values('Services').distinct()
        for fake_address_obj in fake_address_objs:
            payload.append((fake_address_obj['Services']))

    return JsonResponse({'status':200, 'data':payload})
# utillity
class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Dashboard"
        greeting['pageview'] = "Dashboards"        
        return render(request, 'dashboard/dashboard.html',greeting)


class SaasView(LoginRequiredMixin,View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Saas"
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-saas.html',greeting)

class CryptoView(LoginRequiredMixin,View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Crypto" 
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-crypto.html',greeting)

class BlogView(LoginRequiredMixin,View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Blog" 
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-blog.html',greeting)

class CalendarView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "TUI Calendar"
        greeting['pageview'] = "Calendars"
        return render (request, 'calendar.html',greeting)
class CalendarFullView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Full Calendar"
        greeting['pageview'] = "Calendars"
        return render (request, 'calendar-full.html',greeting)
class ChatView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Chat"
        greeting['pageview'] = "Apps"
        return render (request, 'chat-view.html',greeting)

class FileManagerView(LoginRequiredMixin,View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "File Manager"
        greeting['pageview'] = "Apps"
        return render (request,'filemanager.html',greeting)

# Authentication
class PagesLoginView(View):
    def get(self, request):
        return render(request, 'authentication/pages-login.html')
class PagesRegisterView(View):
    def get(self, request):
        return render(request, 'authentication/pages-register.html')
class PagesRecoverpwView(View):
    def get(self, request):
        return render(request, 'authentication/pages-recoverpw.html')
class PagesLockscreenView(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen.html')

class PagesConfirmmailView(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail.html')

class PagesEmailVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail.html')

class PagesTwoStepVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail.html')
class PagesLogin2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-login-2.html')
class PagesRegister2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-register-2.html')
class PagesRecoverpw2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-recoverpw2.html')
class PagesLockscreen2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen2.html')

class PagesConfirmmail2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail-2.html')

class PagesEmailVerification2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail-2.html')

class PagesTwoStepVerification2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail-2.html')

class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard')
class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('dashboard')