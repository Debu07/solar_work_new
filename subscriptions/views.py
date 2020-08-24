from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='landing:login')
def home(request):
    return render(request,'subscriptions/join.html')

@login_required(login_url='landing:login')
def checkout(request):
    return render(request,'subscriptions/checkout.html')


# def paymentView(request):
#     user_membership=get_user_membership(request)
#     selected_membership=get_selected_membership(request)
#     publishKey=settings.STRIPE_PUBLISHABLE_KEY
#     if request.method =='POST':
#         try: 
#             token=request.POST['stripeToken']
#             subscription=stripe.Subscription.create(
#                 customer= user_membership.stripe_customer_id,
#                 items=[
#                     {
#                         "plan":selected_membership.stripe_plan_id,
#                     },
#                 ],
#                 source=token
#             )

#             return redirect(reverse('membership:update_transaction', 
#                     kwargs={
#                         'subscription_id':subscription.id

#             }))



#         except: stripe.CardError as e:
#             messages.info(request,"Your Card Has Been Declined")

#     context={
#         'publishKey':publishKey,
#         'selected_membership':selected_membership
#     }
#     return render(request,'subscriptions/membership_payment.html',context)



# def updateTransactions(request,subscription_id):
#     user_membership=get_user_membership(request)
#     selected_membership=get_selected_membership(request)

#     user_membership.membership=selected_membership
#     user_membership.save()

#     sub, created=Subscription.objects.get_or_create(user_membership=user_membership)
#     sub.stripe_subscription_id=subscription_id
#     sub.active=True
#     sub.save()

#     try:
#         del request.session['selected_membership_type']
#     except:
#         pass

#     messages.info(request,"Successfully Created {}".format(selected_membership))

#     return redirect('/')


# def get_user_membership(request):
#     user_membership_qs=UserMembership.objects.filter(user=request.user)
#     if user_membership_qs.exists():
#         return user_membership_qs.first()
#     return None


# def get_user_subscription(request):
#     user_subscription_qs=Subscription.objects.filter(user_membership=get_user_membership(request))
#     if user_subscription_qs.exists():
#         user_subscription=user_subscription_qs.first()
#         return user_subscription
#     return None


# def get_selected_membership(request):
#     membership_type=request.session['selected_membership_type']
#     selected_membership_qs=Membership.objects.filter(
#         membership_type=membership_type)
#     if selected_membership_qs.exists():
#         return selected_membership_qs.first()
#     return None




# class MembershipSelectView(ListView):
#     model=Membership

#     def get_context_data(self,*args,**kwargs):
#         context= super().get_context_data(**kwargs)
#         current_membership=get_user_membership(self.request)
#         context['current_membership']=str(current_membership.membership)
#         return context

#     def post(self,request,**kwargs):
#         selected_membership=request.POST.get('membership_type')
#         user_membership=get_user_membership(request)
#         user_subscription=get_user_subscription(request)
        
#         selected_membership_qs=Membership.objects.filter(
#             membership_type=selected_membership
#         )
#         if selected_membership_qs.exists():
#             selected_membership=selected_membership_qs.first()

#         ''''
#         ==============
#           VALIDATION
#         ==============
#         '''

#         if user_membership.membership == selected_membership:
#             if user_subscription != None:
#                 messages.info(request,"you already have this membership.\
#                 Your next payment is due {}".format('get this value from stripe'))
#                 return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


#         request.session['selected_membership_type']= selected_membership.membership_type
#         return HttpResponseRedirect(reverse('membership:payment'))