from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


from components.models import Bids, Userdata




#UI-ELEMENTS
class AlertsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Alerts"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-alerts.html',greeting)

class ButtonsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Buttons"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-buttons.html',greeting)

class CardsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Cards"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-cards.html',greeting)    

class CarouselView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Carousel"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-carousel.html',greeting)  


class DropDownsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Dropdowns"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-dropdwons.html',greeting)                    

class GridView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Grid"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-grid.html',greeting) 

class ImagesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Images"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-images.html',greeting)   

class LightBoxView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Lightbox"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-lightbox.html',greeting)    

class ModalsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Modals"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-modals.html',greeting)  

class OffCanvasView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Offcanvas"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-offcanvas.html',greeting)         

class RangeSlidebarView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Range Slider"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-rangeslidebar.html',greeting) 

class SessionTimeoutView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Session Timeout"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-sessiontimeout.html',greeting)           

class ProgressBarsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Progress Bars"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-progressbars.html',greeting)    

class SweetAlertView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Sweet-Alert 2"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-sweetalert.html',greeting)     

class TabsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Tabs & Accordions"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-tabs.html',greeting)   

class TypoGraphyView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Typography"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-typography.html',greeting)   

class VideoView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Video"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-video.html',greeting)   


class GeneralView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "General"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-general.html',greeting)                                                                           

class ColorsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Colors"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-colors.html',greeting)  

class RatingView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Rating"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-rating.html',greeting)  


class NotificationsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Notifications"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-notifications.html',greeting)

class ToastView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Toast"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-toasts.html',greeting)
class PlaceholdersView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Placeholders"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-placeholders.html',greeting)
##FORMS
class FormelementsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Elements"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formelements.html',greeting)


class FormLayoutsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Layouts"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formlayouts.html',greeting)

        
class FormValidationView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Validation"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formvalidation.html',greeting)        

        
class FormAdvancedView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Advanced"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formadvanced.html',greeting)           


class FormEditorsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Editors"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formeditors.html',greeting)         

        
class FormFileuploadView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form File Upload"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formfileupload.html',greeting) 

class FormXeditableView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Xeditable"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formxeditable.html',greeting) 
              
class FormRepeaterView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Repeater"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrepeater.html',greeting) 
           

class FormWizardView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Wizard"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrwizard.html',greeting)                  
        
class FormMaskView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Mask"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrmask.html',greeting)         

        
##Tables

class BasicTablesView(LoginRequiredMixin,View):
    def get(self , request):
        GettingService = Userdata.objects.get(User=request.user)
        Service=GettingService.Services
        print("this is services :", Service)
        words = Service.split('$')
        print(words)

        # bidsData = Bids.objects.all()
        bidsData = Bids.objects.filter(Services__in=words)
        countAllbids=bidsData.count()

        fake_address_objs = Bids.objects.filter().values('Location').distinct()
        payload = []
        for fake_address_obj in fake_address_objs:
            payload.append((fake_address_obj['Location']))
        print(payload)




        # Product.objects.filter(tags__contains=['shoe', 'pant'])
        print(countAllbids)
        # print("this is dropDownServices:",dropDownService)
        context = {
            'Bids': bidsData,
            'countAllbids':countAllbids,
            'dropDownService':words,
            'dropDownLocation':payload
        }
        greeting = {}
        greeting['heading'] = "Active Tenders"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-basictables.html',context)

class DataTablesView(LoginRequiredMixin,View):
    def get(self , request):
        bidsData = Bids.objects.all()
        context = {
            'Bids': bidsData,
        }
        greeting = {}
        greeting['heading'] = "Data Tables"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-datatables.html',context)


class ResponsiveTablesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Responsive Table"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-responsivetables.html',greeting) 

class EditableTablesView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Editable Table"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-editabletables.html',greeting) 

#Charts     
class ApexChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Apex Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-apexcharts.html',greeting)  

class EChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "E Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-echarts.html',greeting)  

class ChartJsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Chartjs Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-chartjs.html',greeting)  

class FlotChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Flot Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-flotcharts.html',greeting)    


class ToastUiChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Toast UI Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-toastuicharts.html',greeting)                  
                         

class JqueryKnobChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Jquery Knob Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-jqueryknobcharts.html',greeting)   

class SparklineChartsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Sparkline Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-sparklinecharts.html',greeting)                                   

#Icons        
class BoxIconsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Boxicons"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-boxicons.html',greeting)         
        

class MaterialDesignView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Material Design"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-materialdesign.html',greeting)    


class DripIconsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Dripicons"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-dripicons.html',greeting)  

class FontAwesomeView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Font Awesome"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-fontawesome.html',greeting)                     

#Maps
class GoogleMapsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Google Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-googlemaps.html',greeting) 

class VectorMapsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Vector Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-vectormaps.html',greeting)      

class LeafletMapsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Leaflet Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-leafletmaps.html',greeting)            
        