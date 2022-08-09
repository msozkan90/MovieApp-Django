from django.shortcuts import render
from .models import Film,Category,Actor, Film_rate
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    films=Film.objects.all()
    actors=Actor.objects.all()
    context={"films":films,"actors":actors}
    return render(request,"index.html",context)

def movies(request):
    rates=Film_rate.objects.all()
    films=Film.objects.all()
    film_list=[]
    film_list2=[]
    rate_film=[]
    for i in rates: 
        if (i.title.title):

          if (str(i.title.title) in str(film_list2)):
            print("")
          else:
              film_list.append(i)
              film_list2.append(i.title.title)
        else:
            
            film_list.append(i)
            film_list2.append(i.title.title)
    for i in films:
            if str(i) in film_list2:
                print(i)
            else:
                film=Film.objects.filter(title=i)
                rate_film.append(i)

    

    context={"films":films,"rates":rates,"film_list":film_list,"rate_film":rate_film}
    return render(request,"movies.html",context)

def actors(request):
    actors=Actor.objects.all()
    context={"actors":actors}
    return render(request,"actors.html",context)


def actor_detail(request,slug):
    actors=Actor.objects.filter(slug=slug)
    for i in actors:
        film_list=Film.objects.filter(Cast=i)
    films_lists=[]
    for a in film_list:
      
        films_lists.append(a)   

    context={"actors":actors,"films_lists":films_lists}
    return render(request,"actor_detail.html",context)


def movie_detail(request,slug):
    actors=Actor.objects.all()
    films=Film.objects.filter(slug=slug)
    total_rate=0
    length=0
    for a in films:
        rates=Film_rate.objects.filter(title=a)
        b =rates.all()
    for c in b:
        total_rate+=c.rate
        length+=1
    rate_avg=0
    if length==0:
        pass
    else:
        rate_avg=(total_rate/length)
  
    for i in films:
        casts=i.Cast.all()
    actor_l=[]
    for a in casts:
        actorss=Actor.objects.filter(name=a)
        actor_l.append(actorss)
    actor_lists=[]
    for i in actor_l:
        print(i[0])
        for a in i:           
            actor_lists.append(a)
    for a in films:
        deneme=Film_rate.objects.filter(title=a.id)
        rates2=deneme.update(avg_rate=rate_avg)
    print(rates2)
    context={"films":films,"actors":actors,"actor_lists":actor_lists,"rate_avg":rate_avg,"length":length,"actor_l":actor_l}
    return render(request,"movie_detail.html",context)


def addRate(request):
    data = json.loads(request.body)
    titles = str(data['film'])
    rate = int(data['rate'])
    user = str(data['user'])
    avg = data['avg']
    film=Film.objects.get(title=titles)
    users=request.user
    rates=Film_rate.objects.create(title=film,user=users,rate=rate,avg_rate=avg)

   
    return JsonResponse('Item was added', safe=False)