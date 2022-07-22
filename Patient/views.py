import json
import string
import random
import datetime
from datetime import date
from django.http  import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import P_Detail,P_Appointment,P_Security,P_Disease
from Doctor.models import D_Detail,D_Specialization
import re
# from .sms import sms_view

def registration_view(request):
    if request.method == 'POST':
         data = json.loads(request.body)
         First_Name_r         = data['First_Name']
         Last_Name_r          = data['Last_Name']
         Username_r           = data['Username']
         DOB_r                = data['DOB']
         Email_r              = data['Email']
         Password_r           = data['Password']
         C_Password_r         = data['C_Password']
         Mobile_Number_r      = data['Mobile_Number']
         Gender_r             = data['Gender']
         Government_ID_r      = data['Government_ID']
         Gov_ID_Number_r      = data['Gov_ID_Number']
         Height_r             = data['Height']
         Weight_r             = data['Weight']
         Blood_Group_r        = data['Blood_Group']
         Address_r            = data['Address']
         City_r               = data['City']
         State_r              = data['State']
         Country_r            = data['Country']
         Pincode_r            = data['Pincode']
         Medical_his          = data['Medical_history']
         
         email_condition = "[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,3}$"
         Passport_condition = "[A-Z]{1}[0-9]{7}$"
         DL_condition = "(([A-Z]{2}[0-9]{2})( )|([A-Z]{2}-[0-9]{2}))((19|20)[0-9][0-9])[0-9]{7}$"
         Voter_ID_condition = "[A-Z]{3}[0-9]{7}$"
         Aadhar_condition = "^[2-9]{1}[0-9]{3}[0-9]{4}[0-9]{4}$"
         Pan_condition   = "[A-Z]{5}[0-9]{4}[A-Z]{1}$"
         match = re.search(email_condition,Email_r)
         match1 = re.search(Aadhar_condition,Gov_ID_Number_r)
         match2 = re.search(Voter_ID_condition,Gov_ID_Number_r)
         match3 = re.search(Passport_condition,Gov_ID_Number_r)
         match4 = re.search(DL_condition,Gov_ID_Number_r)
         match5 = re.search(Pan_condition,Gov_ID_Number_r)  
         
         if (not First_Name_r):
             mes = {
             'message': 'First Name Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Last_Name_r):
             mes = {
              'message': 'Last Name Required!!'
             }
             return JsonResponse(mes,status=403,safe=False) 
         if (not Username_r):
             mes = {   
              'message': 'Username Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)

         if (P_Detail.objects.filter(Username = Username_r)):
             mes = {    
             'message': 'Username Already Exists!!'
             }
             return JsonResponse(mes,status=403,safe=False)
        
         if (not DOB_r):
             mes = {   
              'message': 'DOB Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)        
         if (not Email_r):
             mes = {    
             'message': 'Email Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
    

         if (not match):
             mes = {    
             'message': 'Invalid Email!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (P_Detail.objects.filter(Email = Email_r)):
             mes = {    
             'message': 'Email Already Exists!!'
             }
             return JsonResponse(mes,status=403,safe=False)    
         if (not Mobile_Number_r):
             mes = {    
             'message': 'Mobile Number Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Gender_r):
             mes = {      
             'message': 'Gender Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)   
         if (not Address_r):
             mes = {      
             'message': 'Address Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Country_r):
             mes = {      
             'message': 'Country Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not State_r):
             mes = {      
             'message': 'State Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not City_r):
             mes = {      
             'message': 'City Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)        
         if (not Pincode_r):
             mes = {      
             'message': 'Pincode Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not Government_ID_r):
             mes = {      
             'message': 'Government ID Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)   
         if (not Gov_ID_Number_r):
             mes = {      
             'message': 'Government ID Number Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (Government_ID_r=="AADHAR" and not match1):
             mes = {      
             'message': 'Invalid AADHAR  Number!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         elif (Government_ID_r=="VOTER ID" and not match2):
             mes = {      
             'message': 'Invalid VOTER ID Number!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         elif (Government_ID_r=="PASSPORT" and not match3):
             mes = {      
             'message': 'Invalid PASSPORT Number!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         elif (Government_ID_r=="DRIVING LICENCE" and not match4):
             mes = {      
             'message': 'Invalid DRIVING LICENCE Number!!'
             }
             return JsonResponse(mes,status=403,safe=False)        
         elif (Government_ID_r=="PAN" and not match5):
             mes = {      
             'message': 'Invalid PAN CARD Number!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         
         if (P_Detail.objects.filter(Gov_ID_Number = Gov_ID_Number_r)):
             mes = {    
             'message': 'Government Id Already Exists!!'
             }
             return JsonResponse(mes,status=403,safe=False)    
         if (not Password_r):
             mes = {    
             'message': 'Password Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
         if (not C_Password_r):
             mes = {    
             'message': 'Confirm Password Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)    

                          
         if (Password_r != C_Password_r):
             mes = {    
             'message': 'Password do not Match!!'
             }
             return JsonResponse(mes,status=403,safe=False) 
             
         else:
          Password_h = make_password(Password_r)
          new_user = P_Detail(First_Name=First_Name_r, Last_Name=Last_Name_r, Username=Username_r, DOB=DOB_r, Email=Email_r, Password=Password_h,Mobile_Number=Mobile_Number_r, Gender=Gender_r, Government_ID=Government_ID_r, Gov_ID_Number=Gov_ID_Number_r, Height=Height_r, Weight=Weight_r, Blood_Group=Blood_Group_r, Address=Address_r, City=City_r, State=State_r, Country=Country_r, Pincode=Pincode_r,Medical_History=Medical_his)
          new_user.save()
          mes = {  
          'message': 'Patient Registered Successfully'
           }
          return JsonResponse(mes,status=200,safe=False)




def login_view(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        User_l = data['Username']
        Password_l = data['Password']
        if (not User_l):
             mes = {    
             'message': 'Username Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)
        if (not Password_l):
             mes = {    
             'message': 'Password Required!!'
             }
             return JsonResponse(mes,status=403,safe=False)     
        if (P_Detail.objects.filter(Username = User_l).exists()):
                User_list    = P_Detail.objects.filter(Username = User_l)[0]
                Password_c   = User_list.Password
                DOB_p        = User_list.DOB
                Password_cr  = check_password(Password_l , Password_c)
                a=list((string.ascii_letters+string.digits+"!@#$%^&*"))
                s=""
                for i in range(20):
                 b=random.choice(a)
                 s+=b
                x=P_Detail.objects.get(Username=User_l)
                today = date.today()
                age = today.year - DOB_p.year - ((today.month,today.day)<(DOB_p.month,DOB_p.day)) 
                if Password_cr:
                    Secu = P_Security(Patient=x,Username=User_l,Token=s)
                    Secu.save()
                    x.Patient_Age=age
                    x.save(update_fields=['Patient_Age'])
                    mes = { 
                    'message'    :'Login Successful!!',
                    'Token'      :s
                    }
                    return JsonResponse(mes,status=200,safe=False)
                    
                else:
                    mes = {
                    'message':'Wrong Password!!'
                    }
                    return JsonResponse(mes,status=403,safe=False)

        else:
             
             mes = {
             'message':'Invalid User!!'
             }
             return JsonResponse(mes,status=403,safe=False)


def Patient_dash(request):
        if request.method == 'POST':
        
             data = json.loads(request.body)     
             Token_d = data['Token']

             if (P_Security.objects.filter(Token = Token_d).exists()):
               Patient_s       =P_Security.objects.filter(Token = Token_d)[0]
               Username_d      = Patient_s.Username
               User_li      = P_Detail.objects.filter(Username = Username_d)
               User_det     = list(User_li.values('id','First_Name','Last_Name','Username','DOB','Email','Mobile_Number','Gender','Government_ID',        'Gov_ID_Number','Height','Weight','Blood_Group','Patient_Age','Address','City','State','Country','Pincode','Medical_History'))[0]

              
               mes = {      
                    'User_detail'    :User_det
                    }
               return JsonResponse(mes,status=200,safe=False)
             else:   
               mes = {
                        'message':'Invalid Login attempt!'
                     }
               return JsonResponse(mes,status=403,safe=False)


def Patient_Logout(request):
    if request.method == 'POST':
        data = json.loads(request.body)     
        Token_d = data['Token']               
        Secu = P_Security.objects.get(Token=Token_d)
        Secu.delete()
        mes = {      
        'message'    :"Token Deleted!"
        }
        return JsonResponse(mes,status=200,safe=False)               




def Appointment_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Patient_Disease_l  = data['Patient_Disease']
        Appointment_date_l = data['Appointment_date']
        Appointment_time_l = data['Appointment_time']
        id_l               = data['id']
        today = datetime.date.today()
        format = '%Y-%m-%d'
        APP_date = datetime.datetime.strptime(Appointment_date_l,format).date()
        Token_d = data['Token']

        if (P_Security.objects.filter(Token = Token_d).exists()):
             Patient_s       =P_Security.objects.filter(Token = Token_d)[0]
             Username_d      = Patient_s.Username
             if (not Patient_Disease_l):
                  mes = {
                    'message': 'Patient Disease Required!!'
                   }
                  return JsonResponse(mes,status=403,safe=False) 
             if (not Appointment_date_l):
                   mes = { 
                    'message': 'Appointment date Required!!'
                  }
                   return JsonResponse(mes,status=403,safe=False)         
             if (APP_date < today):
                   mes = { 
                    'message': 'Please Choose Upcoming date!!'
                  }
                   return JsonResponse(mes,status=403,safe=False) 
             if (not Appointment_time_l):
                   mes = { 
                    'message': 'Appointment time Required!!'
                    }
                   return JsonResponse(mes,status=403,safe=False)     
    
             if (P_Detail.objects.filter(Username = Username_d).exists()):
    
                  Patient_l=P_Detail.objects.filter(Username=Username_d)[0]
                  App=D_Detail.objects.get(id=id_l)
                  First=App.First_Name
                  Last=App.Last_Name
                  Appointed_Doctor_l="Dr."+First+" "+Last
                  new_appointment = P_Appointment(Patient=Patient_l, Patient_Disease=Patient_Disease_l,Appointment_date=Appointment_date_l,Appointment_time=Appointment_time_l,Appointed_Doctor=Appointed_Doctor_l)
                  new_appointment.save()
    
                  mes = { 
                       'message'   :'Appointment Request Generated!!'
                       }
                  return JsonResponse(mes,status=200,safe=False)

def Payment_view(request):
    if request.method == 'POST':
         data = json.loads(request.body)
         id_d = data['id']
         Patient_s        =P_Appointment.objects.filter(id = id_d)[0]
         id_p             = Patient_s.id
         x = datetime.datetime.now()
         if(P_Appointment.objects.filter(id=id_p,Payment_Status="Pending").exists()):
           obj = P_Appointment.objects.get(id=id_p)
           obj.Payment_Status="Waiting For Approval"
           obj.Payment_Time=x
           obj.save(update_fields=['Payment_Status','Payment_Time'])
           mes = { 
                'message' :'Payment done Successfully!'
               }
           return JsonResponse(mes,status=200,safe=False)

         else:
             mes = { 
                'message' :'Payment Already done!'
               }
             return JsonResponse(mes,status=403,safe=False)


def Specialization_view(request):
    if request.method == 'POST':
        Speci= D_Specialization.objects.all()
        Spec= []
        for i in Speci:
             Spec.append({'Spec':i.Specialization})

        mes = {
                  'Spe' :Spec
              }
        return JsonResponse(mes,status=200,safe=False)

def Doctor_det_sp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Specialization_d = data['Specialization']
        Doctor_data = []
        if(D_Detail.objects.filter(Speciality=Specialization_d).exists()):
           doctor_det = D_Detail.objects.filter(Speciality=Specialization_d)

           for i  in doctor_det:
             Doctor_data.append({"Id":i.id,"F_Name":i.First_Name,"L_Name":i.Last_Name})
           mes = {      
            'Doctor_detail'    :Doctor_data
            }
           return JsonResponse(mes,status=200,safe=False)
        else:
            mes = {  
           'Doctor_detail'    :Doctor_data,         
           'message'    :"No Doctor Available!"
           }
            return JsonResponse(mes,status=200,safe=False)

def Doctor_det(request):
    if request.method == 'POST':
        if(D_Detail.objects.exists()):
           doctor_det = D_Detail.objects.all()
           Doctor_data=list(doctor_det.values('id','First_Name','Last_Name','Speciality'))
           mes = {      
            'Doctor_detail'    :Doctor_data
            }
           return JsonResponse(mes,status=200,safe=False)
        else:
            mes = {         
           'message'    :"No Doctor Available!"
           }
            return JsonResponse(mes,status=200,safe=False)            


def Doctor_fees(request):
     data = json.loads(request.body)
     id_l   = data['id']
     App=D_Detail.objects.get(id=id_l)
     Fees=App.Appointment_fees
     mes = { 
           'Doctor_fees' :Fees
           }
     return JsonResponse(mes,status=200,safe=False)


def Appointment_History(request):
    data = json.loads(request.body)
    Token_d = data['Token']

    if (P_Security.objects.filter(Token = Token_d).exists()):
          Patient_s       =P_Security.objects.filter(Token = Token_d)[0]
          Patient_s       =P_Security.objects.filter(Token = Token_d)[0]
          id_d            = Patient_s.Patient
          Appointment_det=[]
          if(P_Appointment.objects.filter(Patient=id_d).exists()):
           App_His=P_Appointment.objects.filter(Patient=id_d)
      
           Appointment_det     = list(App_His.values('id','Patient_Disease','Appointment_date','Appointment_time','Appointment_Status',      'Appointed_Doctor','Prescription','Payment_Status','App_Rej_Reason','Payment_Time','Appointment_reg_at'))
           Appointment_det.reverse()
            
           mes = {      
                'Appointment_Hist'    : Appointment_det
                }
           return JsonResponse(mes,status=200,safe=False)
          else:
              mes = {      
                'Appointment_Hist'    : Appointment_det,
                'message'             : "No Appointment History!"
                }
              return JsonResponse(mes,status=200,safe=False)  


def Time_Change(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        A_id = data['id']
        Patient_s        =P_Appointment.objects.filter(id = A_id)[0]
        id_p             = Patient_s.id
        Appointment_p    = Patient_s.Appointment_Status
        
        if(Appointment_p=="Pending" or Appointment_p=="Waiting For Doctor's Approval"):
         if(P_Appointment.objects.filter(id=id_p).exists()):
           App_date= data['Appoint_date']
           App_time= data['Appoint_time']
           today = datetime.date.today()
           format = '%Y-%m-%d'
           APP_date = datetime.datetime.strptime(App_date,format).date()
           if (not App_date):
                   mes = { 
                    'message': 'Appointment date Required!!'
                  }
                   return JsonResponse(mes,status=403,safe=False)
           if (APP_date < today):
                   mes = { 
                    'message': 'Please Choose Upcoming date!!'
                  }
                   return JsonResponse(mes,status=403,safe=False)        
           if (not App_time):
                   mes = { 
                    'message': 'Appointment time Required!!'
                    }
                   return JsonResponse(mes,status=403,safe=False)

           obj = P_Appointment.objects.get(id=id_p)
           x = datetime.datetime.now()
           obj.Appointment_date=App_date
           obj.Appointment_time=App_time
           obj.Appointment_mod_at=x
           obj.save(update_fields=['Appointment_date','Appointment_time','Appointment_mod_at'])
           mes = { 
                'message' :'Appointment Detail Updated!'
               }
           return JsonResponse(mes,status=200,safe=False)
        else:
         mes = { 
                'message' :"Appointment Already Approved Can't Update!"
               }
         return JsonResponse(mes,status=200,safe=False)





def Prescription_det(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        if (P_Security.objects.filter(Token = Token_d).exists()):
            Patient_s  =P_Security.objects.filter(Token = Token_d)[0]
            Username_d      = Patient_s.Username
            Patient_l         = P_Detail.objects.filter(Username = Username_d)[0]
            P_id = Patient_l.id
            Patient_det= []
            if(P_Appointment.objects.filter(Patient = P_id,Appointment_Status="Visited").exists()):
                App = P_Appointment.objects.filter(Patient = P_id,Appointment_Status="Visited")

                
                for i  in App:

                  Patient_det.append({"Id":i.id,"App_date":i.Appointment_date,"App_Doc":i.Appointed_Doctor,"App_time":i.Appointment_time})
                Patient_det.reverse()
                mes = {
                              'Patient_detail' :Patient_det 
                           }
                return JsonResponse(mes,status=200,safe=False)
            else:
                mes = { 
                        'Patient_detail' :Patient_det,
                        'message' :'No Previous Prescription!' 
                     }
                return JsonResponse(mes,status=200,safe=False)


def Prescription_view(request):
     if request.method == 'POST':
        data = json.loads(request.body)
        id_d = data['id']


        App = P_Appointment.objects.filter(id = id_d,Appointment_Status="Visited")[0]
        App_Doctor = App.Appointed_Doctor
        Doc = D_Detail.objects.filter(Display_Name=App_Doctor)[0]

        Patient_det= []
           

        Patient_det.append({"F_Name":App.Patient.First_Name,"L_Name":App.Patient.Last_Name,"User":App.Patient.Username,"App_date":App.Appointment_date,"Pat_disease":App.Patient_Disease,"Pat_Age":App.Patient.Patient_Age,"Gen":App.Patient.Gender,"Diag":App.Diagnosis,"Pres":App.Prescription,"App_Doc":App_Doctor,"Doc_Quali":Doc.Qualification,"Doc_Spec":Doc.Speciality,"Doc_Email":Doc.Email,"Doc_Mobile":Doc.Mobile_Number})   


        mes = {
                'Patient_detail' :Patient_det
              }
        return JsonResponse(mes,status=200,safe=False)




def Payment_History(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_d = data['Token']
        if (P_Security.objects.filter(Token = Token_d).exists()):
            Patient_s  =P_Security.objects.filter(Token = Token_d)[0]
            Username_d      = Patient_s.Username
            Patient_l         = P_Detail.objects.filter(Username = Username_d)[0]
            P_id = Patient_l.id
            Patient_det= []
            if(P_Appointment.objects.filter(Patient = P_id,Payment_Status="Successful").exists()):
                App = P_Appointment.objects.filter(Patient = P_id,Payment_Status="Successful")
                
                for i  in App:

                  Patient_det.append({"Id":i.id,"App_date":i.Appointment_date,"App_Doc":i.Appointed_Doctor,"App_time":i.Appointment_time,"Pay_time":i.Payment_Time})
                Patient_det.reverse()
                mes = {
                              'Patient_detail' :Patient_det
                           }
                return JsonResponse(mes,status=200,safe=False)
            else:    
                mes = {
                        'Patient_detail' :Patient_det,
                        'message'        :"No Payment History!"
                      }
                return JsonResponse(mes,status=200,safe=False)        


def Payment_Receipt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        P_id = data['id']

    
        App = P_Appointment.objects.filter(id = P_id,Payment_Status="Successful")[0]
        Doctor_n = App.Appointed_Doctor
        print(App)
        print(Doctor_n)
        Doc = D_Detail.objects.filter(Display_Name=Doctor_n)[0]
        Patient_det= []
               

        Patient_det.append({"F_Name":App.Patient.First_Name,"L_Name":App.Patient.Last_Name,"App_date":App.Appointment_date,"App_Doc":Doctor_n,"Doc_fees":Doc.Appointment_fees,"App_time":App.Appointment_time,"Pay_time":App.Payment_Time})
        mes = {
              'Patient_detail' :Patient_det
             }
        return JsonResponse(mes,status=200,safe=False)



def Disease_reg(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Disea =data['Disease']

        new_Dise = P_Disease(Disease=Disea)
        new_Dise.save()
        mes = {
                  'message' :"Disease added Successfully!"
              }
        return JsonResponse(mes,status=200,safe=False)

def Disease_view(request):
    if request.method == 'POST':
        Dise = P_Disease.objects.all()
        Disease= []
        for i in Dise:
             Disease.append({'Disea':i.Disease})

        mes = {
                  'Des' :Disease
              }
        return JsonResponse(mes,status=200,safe=False)




# def send_sms(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         User_l = data['Username']
#         if (P_Detail.objects.filter(Username = User_l).exists()):   
#             sms_view(User_l)
#             # a=list((string.digits))
#             # s=""
#             # for i in range(6):
#             #     b=random.choice(a)
#             #     s+=b
#             # x=P_Detail.objects.get(Username=User_l)
#             # Secu = P_Security(Patient=x,Username=User_l,OTP=s)
#             # Secu.save()
#             mes = {
#                   'message' :"Sms Sent Successfully!",
#               }
#             return JsonResponse(mes,status=200,safe=False)
#         else:
#             mes = {
#                   'message' :"Username Doesnot exists!"
#               }
#             return JsonResponse(mes,status=403,safe=False)      


def Password_Change(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Token_l = data['Token']
        
        if (P_Security.objects.filter(Token = Token_l).exists()):
            Patient_s = P_Security.objects.filter(Token = Token_l)[0]
            User_l = Patient_s.Username
            Previous_Pass = data['Previous_Password']
            if (not Previous_Pass):
                        mes = { 
                                'message': 'Previous Password Required!!'
                                 }
                        return JsonResponse(mes,status=403,safe=False)
            if (P_Detail.objects.filter(Username = User_l).exists()):
                User_list    = P_Detail.objects.filter(Username = User_l)[0]
                Password_c   = User_list.Password
                Password_cr  = check_password(Previous_Pass , Password_c)
                if (Password_cr):
                    Password_r    = data['Password']
                    C_Password_r  = data['C_Password']
                    if (not Password_r):
                        mes = { 
                    'message': 'New Password Required!!'
                     }
                        return JsonResponse(mes,status=403,safe=False)
                    if (not C_Password_r):
                        mes = { 
                                 'message': 'Confirm Password Required!!'
                              }
                        return JsonResponse(mes,status=403,safe=False)

                    if(Previous_Pass == Password_r):
                        mes = { 
                                'message' :'Please Enter different Password!!'
                              }
                        return JsonResponse(mes,status=403,safe=False)    
                        
                    if(Password_r != C_Password_r):
                        mes = { 
                                'message' :'Password donot Match!!'
                              }
                        return JsonResponse(mes,status=403,safe=False)
                        

                    else:    
                        Password_h = make_password(Password_r)
                        obj = P_Detail.objects.get(Username = User_l)
                        x = datetime.datetime.now()
                        obj.Password=Password_h
                        obj.modified_at=x
                        obj.save(update_fields=['Password','modified_at'])
                        mes = { 
                            'message' :'Password Changed Successfully!'
                        }
                        return JsonResponse(mes,status=200,safe=False)

                else:
                      mes = { 
                         'message' :'Previous Password doesnot Match!!'
                   }
                return JsonResponse(mes,status=403,safe=False)  


# def OTP_Verification(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         otp_l = data['OTP']
#         if (P_Security.objects.filter(OTP = otp_l).exists()):
#             mes = { 
#                 'message' :'Password donot Match!!'
#                }
#             return JsonResponse(mes,status=403,safe=False)

#         else:
#             mes = { 
#                 'message' :'Incorrect OTP!!'
#                }
#             return JsonResponse(mes,status=403,safe=False)        
                



        
                   


        


      



        
       

  
        
         