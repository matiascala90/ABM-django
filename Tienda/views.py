from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Compania,Plataforma,Genero,Juego
from .forms import CompaniaForm,PlataformaForm,GeneroForm,JuegoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#Home
def home(request):
    return render(request,'home.html')

#Registro de usuario
def registrarse(request):
    if request.method=='GET':
        return render(request,'registrarse.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
              #Registrar Usuario
              usuario=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
              usuario.save()
              login(request,usuario)
              return  redirect('juegos')
            except:
                      return render(request,'registrarse.html',{
                     'form':UserCreationForm,
                     'error':'El usuario ya existe'
                    }) 
        else:
             return render(request,'registrarse.html',{
                     'form':UserCreationForm,
                     'error':'contraseñas no coinciden'
                    }) 

#Iniciar Sesión
def logIn(request):
    if request.method=='GET':
        return render(request,'login.html',{
            'form':AuthenticationForm
        })
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
             return render(request,'login.html',{
            'form':AuthenticationForm,
            'error':'usuario o password incorrecto'
            })
        else:
            login(request,user)
            return redirect('juegos')
#Cerrar Sesión        
@login_required                
def logOut(request):
    logout(request)
    return redirect('home')                
    
#Juegos
@login_required
def juegos(request):
    juegos=Juego.objects.all()
    return render(request,'juegos.html',{
        'juegos':juegos
    })
 #detalle Juego   
@login_required
def juegos_detalle(request,juego_id):
    if request.method=='GET':
       juego=get_object_or_404(Juego,pk=juego_id)
       form=JuegoForm(instance=juego)
       return render(request,'juegos_detalle.html',{'juegos':juego,
      'form':form    
      })
    else:
       try:
           juego=get_object_or_404(Juego,pk=juego_id)
           form=JuegoForm(request.POST,instance=juego)
           form.save()
           return redirect('juegos')
       except ValueError:
            return render(request,'juegos_detalle.html',{'juegos':juegos,
      'form':form ,'error':'Error actualizando el juego'   
      }) 
#Eliminar Juego            
@login_required
def delete_juego(request,juego_id):
    juego=get_object_or_404(Juego,pk=juego_id)     
    if request.method=='POST':
        juego.delete()
        return redirect('juegos')
                   
#Companias
@login_required
def compania(request):
    companias=Compania.objects.all()
    return render(request,'companias.html',{
        'companias':companias
        })
@login_required    
def crear_compania(request):
    if request.method=='GET':
         return render(request,'crear_compania.html',{
        'form':CompaniaForm
       })
    else:
        try:
            form=CompaniaForm(request.POST)
            form.save()
            return redirect('company')
        except ValueError:
             return render(request,'crear_compania.html',{
              'form':CompaniaForm,
              'error':'Verfique que los datos este correctos'
       })              
#Plataforma
@login_required
def plataforma(request):
    plataformas=Plataforma.objects.all()
    return render(request,'plataforma.html',{
        'plataformas':plataformas
    })
#Crear Plataforma    
@login_required
def crear_plataforma(request):
    if request.method=='GET':
         return render(request,'crear_plataforma.html',{
        'form':PlataformaForm
       })
    else:
        try:
            form=PlataformaForm(request.POST)
            form.save()
            return redirect('plataform')
        except ValueError:
             return render(request,'crear_plataforma.html',{
              'form':PlataformaForm,
              'error':'Verfique que los datos este correctos'
       })              
#Generos
@login_required
def genero(request):
    generos=Genero.objects.all()
    return render(request,'genero.html',{
        'generos':generos
    })
#Crear Genero    
@login_required    
def crear_genero(request):
    if request.method=='GET':
        return render(request,'crear_genero.html',{
            'form':GeneroForm
        })
    else:
        try:
            form=GeneroForm(request.POST)
            form.save()
            return redirect('gender')    
        except ValueError:
            return render(request,'crear_genero.html',{
            'form':GeneroForm,
            'error':'Valide si los datos son correctos'
        })
#crear Juego            
@login_required            
def Crear_juego(request):
    if request.method=='GET':
        return render(request,'crear_juegos.html',{
            'form':JuegoForm
        })
    else:
        try:
            form=JuegoForm(request.POST,request.FILES) 
            form.save()
            return redirect('juegos')
        except ValueError:
            return render(request,'crear_juegos.html',{
            'form':JuegoForm,
            'error':'Valide si los datos son correctos'
        })
#Detalle Compania            
@login_required                 
def compania_detalle(request,compania_id):
    if request.method=='GET':
        company=get_object_or_404(Compania,pk=compania_id)
        form=CompaniaForm(instance=company)
        return render(request,'compania_detalle.html',{
            'company':company,
            'form':form
        })
    else:
      try:
           company=get_object_or_404(Compania,pk=compania_id)
           form=CompaniaForm(request.POST,instance=company)
           form.save()
           return redirect('company')
      except ValueError:
            return render(request,'compania_detalle.html',{'company':company,
      'form':form ,'error':'Error actualizando el juego'   
      }) 
#Eliminar compania            
@login_required
def delete_compania(request,compania_id):
    company=get_object_or_404(Compania,pk=compania_id)     
    if request.method=='POST':
        company.delete()
        return redirect('company')   
      
 #Detalle Plataforma   
@login_required                 
def plataforma_detalle(request,plataforma_id):
    if request.method=='GET':
        plataform=get_object_or_404(Plataforma,pk=plataforma_id)
        form=PlataformaForm(instance=plataform)
        return render(request,'plataforma_detalle.html',{
            'plataform':plataform,
            'form':form
        })
    else:
      try:
           plataform=get_object_or_404(Plataforma,pk=plataforma_id)
           form=PlataformaForm(request.POST,instance=plataform)
           form.save()
           return redirect('plataform')
      except ValueError:
            return render(request,'plataforma_detalle.html',{'plataform':plataform,
      'form':form ,'error':'Error actualizando el juego'   
      }) 
#Eliminar Plataforma            
@login_required
def delete_plataforma(request,plataforma_id):
    plataform=get_object_or_404(Plataforma,pk=plataforma_id)     
    if request.method=='POST':
        plataform.delete()
        return redirect('plataform')  
                         
 #Detalle Genero       
@login_required                 
def genero_detalle(request,genero_id):
    if request.method=='GET':
        gender=get_object_or_404(Genero,pk=genero_id)
        form=GeneroForm(instance=gender)
        return render(request,'genero_detalle.html',{
            'gender':gender,
            'form':form
        })
    else:
      try:
           gender=get_object_or_404(Genero,pk=genero_id)
           form=GeneroForm(request.POST,instance=gender)
           form.save()
           return redirect('gender')
      except ValueError:
            return render(request,'genero_detalle.html',{'gender':gender,
      'form':form ,'error':'Error actualizando el juego'   
      }) 
#Eliminar Genero            
@login_required
def delete_genero(request,genero_id):
    gender=get_object_or_404(Genero,pk=genero_id)     
    if request.method=='POST':
        gender.delete()
        return redirect('gender')                       
                                                             