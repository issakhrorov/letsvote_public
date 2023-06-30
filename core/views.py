from .models import Category, Element, Promotion, Vote, Voter
from django.contrib.auth.models import User, auth
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .serializers import CategorySerializer, PromotionSerializer, ElementSerializer
from django.contrib import messages
from django.shortcuts import render, redirect

@api_view(['GET'])
def getElements(request):
  elements = Element.objects.all()
  serializer = ElementSerializer(elements, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getCategory(request):
  category_names = Category.objects.all()
  serializer = CategorySerializer(category_names, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def getActivePromotions(request):
  # filtered active promotions
  elements = []
  battles = Promotion.objects.filter(status='Promotion')
  serializer = PromotionSerializer(battles, many=True)
  for battle in serializer.data:
    left = battle['left_elem']
    right = battle['right_elem']
    left_elem = Element.objects.get(id=left)
    right_elem = Element.objects.get(id=right)

    elements.append({'left_elem': left_elem.image.url, 'right_elem': right_elem.image.url, 'battle_name': battle['promotion'], 'battle_description': battle['description'], 'battle': battle['id']})
 
  return Response(elements)

@api_view(['GET'])
def getCategoryPromotions(request, pk):
  elements = []
  category = Category.objects.filter(id=pk).first()
  battles = Promotion.objects.filter(category=category.id)
  serializer = PromotionSerializer(battles, many=True)
  for battle in serializer.data:
    if battle['status'] == 'Promotion' or 'Ended':
      left = battle['left_elem']
      right = battle['right_elem']
      left_elem = Element.objects.get(id=left)
      right_elem = Element.objects.get(id=right)

      elements.append({
        'left_elem': left_elem.image.url, 
        'right_elem': right_elem.image.url, 
        'battle_name': battle['promotion'], 
        'battle_description': battle['description'], 
        'battle': battle['id']
      })
 
  return Response(elements)

@api_view(['GET'])
def getCards(request, pk):
  cards = []
  # card
  battle = Promotion.objects.get(id=pk)
  left_elem = Element.objects.get(element_name=battle.left_elem)
  right_elem = Element.objects.get(element_name=battle.right_elem)

  left_serializer = ElementSerializer(left_elem, many=False)
  right_serializer = ElementSerializer(right_elem, many=False)

  # votes count
  left_vote = Vote.objects.filter(element_id=left_elem.id).first()
  right_vote = Vote.objects.filter(element_id=right_elem.id).first()

  if left_vote != None:
    left_vote_count = left_vote.votes_count
  else:
    left_vote_count = 0

  if right_vote != None:
    right_vote_count = right_vote.votes_count
  else:
    right_vote_count = 0

  # g = GeoIP2()
  # voter_country = g.city(ip)
  # new_voter = Voter.objects.create(ip=ip)

  cards.append({
    'battle': battle.id,
    'left_elem': left_serializer.data,
    'right_elem': right_serializer.data,
    'left_vote_count': left_vote_count,
    'right_vote_count': right_vote_count
  })
  
  return Response(cards)

@api_view(['GET'])
def getInfo(request, pk):
  card = Element.objects.get(id=pk)
  serializer = ElementSerializer(card, many=False)
  return Response(serializer.data)

@api_view(['GET', 'POST'])
def getVote(request):
  if request.method == 'POST':
    left = request.data['left']
    left_element = Element.objects.get(id=left)    
    promotion = Promotion.objects.get(left_elem=left_element)
    right_element = Element.objects.get(element_name=promotion.right_elem)
    left_vote = Vote.objects.filter(element_id=left_element.id).first()
    right_vote = Vote.objects.filter(element_id=right_element.id).first()
    right_votes_count = len(Voter.objects.filter(element_id=right_element.id))
    left_votes_count = len(Voter.objects.filter(element_id=left_element.id))
      
    # assign voter
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    voter = Voter.objects.filter(ip=ip, promotion_id=promotion.id).first()

    if voter == None:
      voter = Voter.objects.create(ip=ip, element_id=left_element.id, promotion_id = promotion.id)
      if left_vote == None:
        left_vote = Vote.objects.create(element_id=left_element.id)
      left_votes_count = len(Voter.objects.filter(element_id=left_element.id))
      left_vote.votes_count = left_votes_count
      left_vote.save()
    elif voter:
      if int(voter.element_id) == int(left_element.id):
        voter.delete()

        left_votes_count = len(Voter.objects.filter(element_id=left_element.id))
        left_vote.votes_count = left_votes_count
        left_vote.save()

      elif int(voter.element_id) == int(right_element.id):
        voter.element_id = left_element.id
        voter.save()
        if left_vote == None:
          left_vote = Vote.objects.create(element_id=left_element.id)
        left_votes_count = len(Voter.objects.filter(element_id=left_element.id))
        left_vote.votes_count = left_votes_count
        left_vote.save()

        right_votes_count = len(Voter.objects.filter(element_id=right_element.id))
        right_vote.votes_count = right_votes_count
        right_vote.save()
      
    if right_votes_count == None:
      right_votes_count = 0
    if left_votes_count == None:
      left_votes_count = 0

    response_data = {
      'left_votes_count': left_votes_count,
      'right_votes_count': right_votes_count
    }

    return Response({"message": "Got some data!", "data": response_data})

  return Response({"message": request.data})

@api_view(['GET', 'POST'])
def getRightVote(request):
  if request.method == 'POST':
    right = request.data['right']
    right_element = Element.objects.get(id=right)    
    promotion = Promotion.objects.get(right_elem=right_element)
    left_element = Element.objects.get(element_name=promotion.left_elem)
    right_vote = Vote.objects.filter(element_id=right_element.id).first()
    left_vote = Vote.objects.filter(element_id=left_element.id).first()
    right_votes_count = len(Voter.objects.filter(element_id=right_element.id))
    left_votes_count = len(Voter.objects.filter(element_id=left_element.id))

    # assign voter
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    voter = Voter.objects.filter(ip=ip, promotion_id=promotion.id).first()

    if voter == None:
      voter = Voter.objects.create(ip=ip, element_id=right_element.id, promotion_id = promotion.id)
      if right_vote == None:
        right_vote = Vote.objects.create(element_id=right_element.id)
      right_votes_count = len(Voter.objects.filter(element_id=right_element.id))
      right_vote.votes_count = right_votes_count
      right_vote.save()

    elif voter:
      if int(voter.element_id) == int(right_element.id):
        voter.delete()

        right_votes_count = len(Voter.objects.filter(element_id=right_element.id))
        right_vote.votes_count = right_votes_count
        right_vote.save()

      elif int(voter.element_id) == int(left_element.id):
        voter.element_id = right_element.id
        voter.save()
        if right_vote == None:
          right_vote = Vote.objects.create(element_id=right_element.id)
        right_votes_count = len(Voter.objects.filter(element_id=right_element.id))
        right_vote.votes_count = right_votes_count
        right_vote.save()

        left_votes_count = len(Voter.objects.filter(element_id=left_element.id))
        left_vote.votes_count = left_votes_count
        left_vote.save()

    if left_votes_count == None:
      left_votes_count = 0 
    if right_votes_count == None:
      right_votes_count = 0

    response_data = {
      'left_votes_count': left_votes_count,
      'right_votes_count': right_votes_count
    }
    return Response(response_data)

  return Response({"message": request.data})

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']  
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email Taken')
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username Taken')
        return redirect('signup')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)
        return redirect('settings')
    else: 
      messages.info(request, 'Password Not Matching')
      return redirect('signup') 
  else:
    return render(request, 'signup.html')

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Credentials Invalid')
      return redirect('signin')
  else:
    return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
  auth.logout(request)
  return redirect('signin')