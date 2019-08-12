from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    # return HttpResponse('<h1>홈페이지</h1>') #pass
    name = '이한얼'
    data = ['이한얼','정의진']
    empty_data = ['엄복동', '클레멘타인']
    matrix = [[1,2,3],[4,5,6]]
    context = {
        'name': name,
        'data': data,
        'empty_data': empty_data,
        'matrix': matrix,
    }

    # return render(request, 'home.html', name=name)
    return render(request, 'home.html', context, {'name2': '이한얼'})

import random
def lotto(request):
    # lottoList = random.choices()
    # lottoList=list(map(str,random.randint(range(1,46),6)))
    lottoList=random.sample(range(1,46),6)
    nums = lottoList
    context = {
        'nums': nums,
        'number': 'lotto!',
    }
    return render(request, 'lotto.html', context)

def cube(request, num):
    result = num ** 3
    context = {
        'result': result,
    }
    return render(request, 'cube.html', context)

# input 과 form을 이용해서 넘기기
def match(request):
    import random
    goonghap = random.randint(50,100)
    # me = request.GET.get('me')
    # you = request.GET.get('you')
    print(request)
    print(request.GET)
    print(request.POST)
    me = request.POST.get('me') # flask에서의 request.get('me') 와 유사!
    you = request.POST.get('you')

    test = request.get_host() # host에 대한 값이 들어감
    # print(request.get())
    # 딕셔너리와 비슷한 쿼리 딕트가 들어옴,  'me', 'you'라는 객체가 들어온다.
    context = {
        'goonghap': goonghap,
        'me': me,
        'you': you,
        'test': test,
    }
    return render(request,'match.html', context)