from django.shortcuts import render
from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.

# Create your views here.
def index(request):
    return render(request,'index.html')
def emplogin(request):
    error=""
    t=""
    if request.method =="POST":
        u=request.POST['email']
        p=request.POST['password']
        
        user=authenticate(request,username=u,password=p)
        
        if user:
            emp=EmployeeDetail.objects.get(user=user)
            if emp.stafftype=="Teaching Staff":
                t="TS"
            else:
                t="NTS"

            print(emp.stafftype)
            login(request,user)
            error="no"
        else:
            error="yes"

    return render(request,'emplogin.html',locals())
    
def adminlogin(request):
    return render(request,'adminlogin.html')
def empsignup(request):
    error=""
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        eid=request.POST['employeeid']
        email=request.POST['emailid']
        pwd=request.POST['password']
        stype=request.POST['type']
        try:
            user=User.objects.create_user(first_name=fname,last_name=lname,username=email,password=pwd)
            EmployeeDetail.objects.create(user=user,empid=eid,stafftype=stype)
            if stype=="Non Teaching Staff":
                NonTeachingEmployee.objects.create(user=user)
            #EmployeeExperience.objects.create(user=user)
            #EmployeeEducation.objects.create(user=user)
            if stype=="Teaching Staff":
                TeachingEmployee.objects.create(user=user)
            error="no"
        except:
            error="yes"
        
    return render(request,'empsignup.html',locals())
#def employeehome(request):
    #return render(request,'employeehome.html')
def employeehomeNTS(request):
    error=""
    a=""
    p=""
    if not request.user.is_authenticated:
        return redirect('employeelogin')
    user=request.user
    employee=EmployeeDetail.objects.get(user=user)
    emp=NonTeachingEmployee.objects.get(user=user)
    if employee.pan:
        p=employee.pan
        p=p[:6]+"XXXX"
    if employee.adhar:
        a=employee.adhar
        a=a[:8]+"XXXX"
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        dob=request.POST['DOB']
        altemail=request.POST['altemail']
        mob=request.POST['mob']
        altmob=request.POST['altmob']
        gender=request.POST['gender']
        adhar=request.POST['adhar']
        pan=request.POST['pan']
        mstatus=request.POST['marital Status']
        bg=request.POST['bloodgroup']
        eid=request.POST['eid']
        joiningdate=request.POST['jd']
        wl=request.POST["wl"]
        desg=request.POST['des']
        twe=request.POST["twe"]
        dept=request.POST['department']
        presenthn=request.POST["presenthn"]
        presentsn=request.POST["presentsn"]
        presentcn=request.POST["presentcn"]
        presentdn=request.POST["presentdn"]
        presentState=request.POST["presentState"]
        presentzip=request.POST["presentzip"]


        permhn=request.POST["permhn"]
        permsn=request.POST["permsn"]
        permcn=request.POST["permcn"]
        permdn=request.POST["permdn"]
        permState=request.POST["permState"]
        permzip=request.POST["permzip"]

        noe10=request.POST["noe10"]
        board10=request.POST["board10"]
        marks10=request.POST["marks10"]
        yop10=request.POST["yop10"]

        noe12=request.POST["noe12"]
        board12=request.POST["board12"]
        marks12=request.POST["marks12"]
        yop12=request.POST["yop12"]

        deg=request.POST["deg"]
        uni=request.POST["uni"]
        marksdeg=request.POST["marksdeg"]
        yopdeg=request.POST["yopdeg"]


        
        #contact=request.POST['contact']
        
        
        
        employee.user.first_name=fname
        employee.user.last_name=lname
        
        
        
        employee.altemail=altemail
        employee.mob=mob
        employee.altmob=altmob
        employee.adhar=adhar
        employee.pan=pan
        #employee.mstatus=mstatus
        #employee.bloodgroup=bg
        employee.empid=eid
        employee.worklocation=wl
        employee.workexperience=twe
        employee.presenthousenum=presenthn
        employee.presentstreet=presentsn
        employee.presentcity=presentcn
        employee.presentdist=presentdn
        #employee.presentstate=presentState
        employee.presentzip=presentzip
        employee.curhousenum=permhn
        employee.curstreet=permsn
        employee.curcity=permcn
        employee.curdist=permdn
        #employee.curstate=permState
        employee.curzip=permzip
        #employee.gender=gender
        #employee.joiningdate=joiningdate
        #employee.DOB=dob


        emp.desg=desg
        emp.dept=dept

        emp.noe10=noe10
        emp.board10=board10
        emp.marks10=marks10
        #emp.yop10=yop10

        emp.noe12=noe12
        emp.board12=board12
        emp.marks12=marks12
        #emp.yop12=yop12
        

        emp.noedegree=deg
        emp.uni=uni
        emp.marksdeg=marksdeg
        #emp.yopdeg=yopdeg
        print(gender)
        
        
        if joiningdate:
            employee.joiningdate=joiningdate
        if gender!="None":
            employee.gender=gender
        if dob:
            employee.DOB=dob
        if yop10:
            emp.yop10=yop10
        if yop12:
            emp.yop12=yop12
        if yopdeg:
            emp.yopdeg=yopdeg
        if mstatus!="None":
            employee.mstatus=mstatus
        if bg!="None":
            employee.bloodgroup=bg
        if dept!="None":
            emp.dept=dept
        if presentState!="None":
            employee.presentstate=presentState
        if permState!="None":
            employee.curstate=permState

        
        try:
            employee.save()
            employee.user.save()
            emp.save()
            emp.user.save()
            error="no"
        except:
            error="yes"

      
    return render(request,'employeehomeNTS.html',locals())
    #return render(request,'employeehomeNTS.html')


def employeehome(request):
    
    error=""
    p=""
    a=""
    if not request.user.is_authenticated:
        return redirect('employeelogin')
    user=request.user
    employee=EmployeeDetail.objects.get(user=user)
    emp=TeachingEmployee.objects.get(user=user)
    if employee.pan:
        p=employee.pan
        p=p[:6]+"XXXX"
    if employee.pan:
        a=employee.adhar
        a=a[:8]+"XXXX"
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        dob=request.POST['DOB']
        altemail=request.POST['altemail']
        mob=request.POST['mob']
        altmob=request.POST['altmob']
        gender=request.POST['gender']
        adhar=request.POST['adhar']
        pan=request.POST['pan']
        mstatus=request.POST['marital Status']
        bg=request.POST['bloodgroup']
        eid=request.POST['eid']
        joiningdate=request.POST['jd']
        wl=request.POST["wl"]
        desg=request.POST['des']
        twe=request.POST["twe"]
        dept=request.POST['department']
        presenthn=request.POST["presenthn"]
        presentsn=request.POST["presentsn"]
        presentcn=request.POST["presentcn"]
        presentdn=request.POST["presentdn"]
        presentState=request.POST["presentState"]
        presentzip=request.POST["presentzip"]


        permhn=request.POST["permhn"]
        permsn=request.POST["permsn"]
        permcn=request.POST["permcn"]
        permdn=request.POST["permdn"]
        permState=request.POST["permState"]
        permzip=request.POST["permzip"]

        noe10=request.POST["noe10"]
        board10=request.POST["board10"]
        marks10=request.POST["marks10"]
        yop10=request.POST["yop10"]

        noe12=request.POST["noe12"]
        board12=request.POST["board12"]
        marks12=request.POST["marks12"]
        yop12=request.POST["yop12"]

        deg=request.POST["deg"]
        uni=request.POST["uni"]
        marksdeg=request.POST["marksdeg"]
        yopdeg=request.POST["yopdeg"]

        npg=request.POST["npg"]
        unipg=request.POST["unipg"]
        markspg=request.POST["markspg"]
        yoppg=request.POST["yoppg"]

        unidoc=request.POST["unidoc"]
        streamdoc=request.POST["streamdoc"]
        dreg=request.POST["dreg"]
        yopdoc=request.POST["yopdoc"]

        unipdoc=request.POST["unipdoc"]
        streampdoc=request.POST["streampdoc"]
        stdate=request.POST["stdate"]
        enddate=request.POST["enddate"]



        
        #contact=request.POST['contact']
        
        
        
        employee.user.first_name=fname
        employee.user.last_name=lname
        
        
        
        employee.altemail=altemail
        employee.mob=mob
        employee.altmob=altmob
        employee.adhar=adhar
        employee.pan=pan
        #employee.mstatus=mstatus
        #employee.bloodgroup=bg
        employee.empid=eid
        employee.worklocation=wl
        employee.workexperience=twe
        employee.presenthousenum=presenthn
        employee.presentstreet=presentsn
        employee.presentcity=presentcn
        employee.presentdist=presentdn
        #employee.presentstate=presentState
        employee.presentzip=presentzip
        employee.curhousenum=permhn
        employee.curstreet=permsn
        employee.curcity=permcn
        employee.curdist=permdn
        #employee.curstate=permState
        employee.curzip=permzip
        #employee.gender=gender
        #employee.joiningdate=joiningdate
        #employee.DOB=dob


        #emp.desg=desg
        #emp.dept=dept

        emp.noe10=noe10
        emp.board10=board10
        emp.marks10=marks10
        #emp.yop10=yop10

        emp.noe12=noe12
        emp.board12=board12
        emp.marks12=marks12
        #emp.yop12=yop12
        

        emp.noedegree=deg
        emp.uni=uni
        emp.marksdeg=marksdeg
        #emp.yopdeg=yopdeg
        print(gender)

        emp.npg=npg
        emp.unipg=unipg
        emp.markspg=markspg

        emp.unidoc=unidoc
        emp.stramdoc=streamdoc

        emp.unipdoc=unipdoc
        emp.strampdoc=streampdoc
        
        
        if joiningdate:
            employee.joiningdate=joiningdate
        if gender!="None":
            employee.gender=gender
        if dob:
            employee.DOB=dob
        if yop10:
            emp.yop10=yop10
        if yop12:
            emp.yop12=yop12
        if yopdeg:
            emp.yopdeg=yopdeg
        if mstatus!="None":
            employee.mstatus=mstatus
        if bg!="None":
            employee.bloodgroup=bg
        if dept!="None":
            emp.dept=dept
        if presentState!="None":
            employee.presentstate=presentState
        if permState!="None":
            employee.curstate=permState
        if desg!="None":
            emp.desg=desg
        if yoppg:
            emp.yoppg=yoppg
        if dreg:
            emp.dreg=dreg
        if yopdoc:
            emp.yopdoc=yopdoc
        if stdate:
            emp.stdate=stdate
        if enddate:
            emp.enddate=enddate
        

        
        try:
            employee.save()
            employee.user.save()
            emp.save()
            emp.user.save()
            error="no"
            
            
        except:
            error="yes"

      
    return render(request,'employeehome.html',locals())

def adminlogin(request):
    error=""
    if request.method =="POST":
        u=request.POST['username']
        p=request.POST['password']
        
        user=authenticate(request,username=u,password=p)
        #print(user)
        if user:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        else:
            error="yes"
    return render(request,'adminlogin.html',locals())
def adminhome(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    employee=EmployeeDetail.objects.all()
    return render(request,'adminhome.html',locals())

def delete_record(request,username):

    emp=User.objects.get(username=username)
    
    emp.delete()
    employee=EmployeeDetail.objects.all()
    return render(request,'adminhome.html',locals())

def admin_edit_emp(request,username):
    error=""
    a=""
    p=""
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    
    user=User.objects.get(username=username)
    employee=EmployeeDetail.objects.get(user=user)
    #print(employee.stafftype)
    if employee.pan:
        p=employee.pan
        p=p[:6]+"XXXX"
    if employee.adhar:
        a=employee.adhar
        a=a[:8]+"XXXX"
        print(a)
    if employee.stafftype=="Non Teaching Staff":
        emp=NonTeachingEmployee.objects.get(user=user)
        if request.method=="POST":
            fname=request.POST['firstname']
            lname=request.POST['lastname']
            dob=request.POST['DOB']
            altemail=request.POST['altemail']
            mob=request.POST['mob']
            altmob=request.POST['altmob']
            gender=request.POST['gender']
            adhar=request.POST['adhar']
            pan=request.POST['pan']
            mstatus=request.POST['marital Status']
            bg=request.POST['bloodgroup']
            eid=request.POST['eid']
            joiningdate=request.POST['jd']
            wl=request.POST["wl"]
            desg=request.POST['des']
            twe=request.POST["twe"]
            dept=request.POST['department']
            presenthn=request.POST["presenthn"]
            presentsn=request.POST["presentsn"]
            presentcn=request.POST["presentcn"]
            presentdn=request.POST["presentdn"]
            presentState=request.POST["presentState"]
            presentzip=request.POST["presentzip"]


            permhn=request.POST["permhn"]
            permsn=request.POST["permsn"]
            permcn=request.POST["permcn"]
            permdn=request.POST["permdn"]
            permState=request.POST["permState"]
            permzip=request.POST["permzip"]

            noe10=request.POST["noe10"]
            board10=request.POST["board10"]
            marks10=request.POST["marks10"]
            yop10=request.POST["yop10"]

            noe12=request.POST["noe12"]
            board12=request.POST["board12"]
            marks12=request.POST["marks12"]
            yop12=request.POST["yop12"]

            deg=request.POST["deg"]
            uni=request.POST["uni"]
            marksdeg=request.POST["marksdeg"]
            yopdeg=request.POST["yopdeg"]

            employee.user.first_name=fname
            employee.user.last_name=lname
        
        
        
            employee.altemail=altemail
            employee.mob=mob
            employee.altmob=altmob
            employee.adhar=adhar
            employee.pan=pan
        #employee.mstatus=mstatus
        #employee.bloodgroup=bg
            employee.empid=eid
            employee.worklocation=wl
            employee.workexperience=twe
            employee.presenthousenum=presenthn
            employee.presentstreet=presentsn
            employee.presentcity=presentcn
            employee.presentdist=presentdn
        #employee.presentstate=presentState
            employee.presentzip=presentzip
            employee.curhousenum=permhn
            employee.curstreet=permsn
            employee.curcity=permcn
            employee.curdist=permdn
        
            employee.curzip=permzip


            emp.desg=desg
            emp.dept=dept

            emp.noe10=noe10
            emp.board10=board10
            emp.marks10=marks10
        

            emp.noe12=noe12
            emp.board12=board12
            emp.marks12=marks12
        
        

            emp.noedegree=deg
            emp.uni=uni
            emp.marksdeg=marksdeg
            if employee.adhar:
                a=employee.adhar
                a=a[:8]+"XXXX"
                print(a)
            if employee.pan:
                p=employee.pan
                p=p[:6]+"XXXX"
        
        
            if joiningdate:
                employee.joiningdate=joiningdate
            if gender!="None":
                employee.gender=gender
            if dob:
                employee.DOB=dob
            if yop10:
                emp.yop10=yop10
            if yop12:
                emp.yop12=yop12
            if yopdeg:
                emp.yopdeg=yopdeg
            if mstatus!="None":
                employee.mstatus=mstatus
            if bg!="None":
                employee.bloodgroup=bg
            if dept!="None":
                emp.dept=dept
            if presentState!="None":
                employee.presentstate=presentState
            if permState!="None":
                employee.curstate=permState
            try:
                employee.save()
                employee.user.save()
                emp.save()
                emp.user.save()
                error="no"
            except:
                error="yes"
        return render(request,"admineditNTS.html", locals())
    if employee.stafftype=="Teaching Staff":
        emp=TeachingEmployee.objects.get(user=user)
        if request.method=='POST':
            fname=request.POST['firstname']
            lname=request.POST['lastname']
            dob=request.POST['DOB']
            altemail=request.POST['altemail']
            mob=request.POST['mob']
            altmob=request.POST['altmob']
            gender=request.POST['gender']
            adhar=request.POST['adhar']
            pan=request.POST['pan']
            mstatus=request.POST['marital Status']
            bg=request.POST['bloodgroup']
            eid=request.POST['eid']
            joiningdate=request.POST['jd']
            wl=request.POST["wl"]
            desg=request.POST['des']
            twe=request.POST["twe"]
            dept=request.POST['department']
            presenthn=request.POST["presenthn"]
            presentsn=request.POST["presentsn"]
            presentcn=request.POST["presentcn"]
            presentdn=request.POST["presentdn"]
            presentState=request.POST["presentState"]
            presentzip=request.POST["presentzip"]


            permhn=request.POST["permhn"]
            permsn=request.POST["permsn"]
            permcn=request.POST["permcn"]
            permdn=request.POST["permdn"]
            permState=request.POST["permState"]
            permzip=request.POST["permzip"]

            noe10=request.POST["noe10"]
            board10=request.POST["board10"]
            marks10=request.POST["marks10"]
            yop10=request.POST["yop10"]

            noe12=request.POST["noe12"]
            board12=request.POST["board12"]
            marks12=request.POST["marks12"]
            yop12=request.POST["yop12"]

            deg=request.POST["deg"]
            uni=request.POST["uni"]
            marksdeg=request.POST["marksdeg"]
            yopdeg=request.POST["yopdeg"]

            npg=request.POST["npg"]
            unipg=request.POST["unipg"]
            markspg=request.POST["markspg"]
            yoppg=request.POST["yoppg"]

            unidoc=request.POST["unidoc"]
            streamdoc=request.POST["streamdoc"]
            dreg=request.POST["dreg"]
            yopdoc=request.POST["yopdoc"]

            unipdoc=request.POST["unipdoc"]
            streampdoc=request.POST["streampdoc"]
            stdate=request.POST["stdate"]
            enddate=request.POST["enddate"]

            employee.user.first_name=fname
            employee.user.last_name=lname
        
            employee.altemail=altemail
            employee.mob=mob
            employee.altmob=altmob
            employee.adhar=adhar
            employee.pan=pan
        
            employee.empid=eid
            employee.worklocation=wl
            employee.workexperience=twe
            employee.presenthousenum=presenthn
            employee.presentstreet=presentsn
            employee.presentcity=presentcn
            employee.presentdist=presentdn
        #employee.presentstate=presentState
            employee.presentzip=presentzip
            employee.curhousenum=permhn
            employee.curstreet=permsn
            employee.curcity=permcn
            employee.curdist=permdn
        #employee.curstate=permState
            employee.curzip=permzip
        

            emp.noe10=noe10
            emp.board10=board10
            emp.marks10=marks10
        #emp.yop10=yop10

            emp.noe12=noe12
            emp.board12=board12
            emp.marks12=marks12
        #emp.yop12=yop12
        

            emp.noedegree=deg
            emp.uni=uni
            emp.marksdeg=marksdeg
            #emp.yopdeg=yopdeg
        

            emp.npg=npg
            emp.unipg=unipg
            emp.markspg=markspg

            emp.unidoc=unidoc
            emp.stramdoc=streamdoc

            emp.unipdoc=unipdoc
            emp.strampdoc=streampdoc

            if employee.adhar:
                a=employee.adhar
                a=a[:8]+"XXXX"
                print(a)
            if employee.pan:
                p=employee.pan
                p=p[:6]+"XXXX"
        
        
            if joiningdate:
                employee.joiningdate=joiningdate
            if gender!="None":
                employee.gender=gender
            if dob:
                employee.DOB=dob
            if yop10:
                emp.yop10=yop10
            if yop12:
                emp.yop12=yop12
            if yopdeg:
                emp.yopdeg=yopdeg
            if mstatus!="None":
                employee.mstatus=mstatus
            if bg!="None":
                employee.bloodgroup=bg
            if dept!="None":
                emp.dept=dept
            if presentState!="None":
                employee.presentstate=presentState
            if permState!="None":
                employee.curstate=permState
            if desg!="None":
                emp.desg=desg
            if yoppg:
                emp.yoppg=yoppg
            if dreg:
                emp.dreg=dreg
            if yopdoc:
                emp.yopdoc=yopdoc
            if stdate:
                emp.stdate=stdate
            if enddate:
                emp.enddate=enddate

        
            try:
                employee.save()
                employee.user.save()
                emp.save()
                emp.user.save()
                error="no"
            except:
                error="yes"

      
        
        return render(request,"admineditTS.html",locals())
        

      
    
def admineditNTS(request,username):
    return render(request,'admineditNTS.html',locals())
def admineditTS(request,username):
    return render(request,'admineditNTS.html',locals())

def adminlogout(request):
    logout(request)
    return redirect('adminlogin')
def logoutemp(request):
    logout(request)
    return redirect('emplogin')
def gobacktoadmin(request):
    return redirect('adminhome')





