from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from finance import * 
from forms import *
from django.template import RequestContext
from models import *
@login_required
def portal_main_page(request):
	user = request.user
	all_stocks = GetAllStocks()
		
	# print '\n\n',all_stocks
	# print type(all_stocks)
	return render_to_response('portal.html',{'user':user,'stock_data':all_stocks})


def company_page(request,symbol):

	def BuyStock(dict1,symbol,count,balance):
		if request.session["price"]*count <= balance:
			print "Have enough balance"
			final_balance = balance - request.session["price"]*count
			if symbol in dict1:
				dict1[symbol]+=count
			else:
				dict1[symbol] = count
			return (dict1,final_balance)
		else:
			return (dict1,balance)

	def SellStock(dict1,symbol,count,balance):
		if symbol in dict1 and dict1[symbol]>=count:
			print "Old balance: ",balance
			final_balance = balance + request.session["price"]*count
			print "New balance: ",final_balance
			if symbol in dict1:
				dict1[symbol]-=count
			return (dict1,final_balance)
		else:
			return (dict1,balance)

	ThisUser = request.user
	temp = GetCompanyDetails(symbol)

	if request.method == 'GET':
		print "new form"
		form = BuyAndSellForm()
		request.session["price"] = float(temp['Ask'])

	else:
		form = BuyAndSellForm(request.POST)
		if form.is_valid():
			SellStocksCountInteger = form.cleaned_data['SellStocksCount']
			BuyStocksCountInteger = form.cleaned_data['BuyStocksCount']
			current_user = UserProfile.objects.get(user = ThisUser)
			user_balance = current_user.balance 
			StocksOwnedString = current_user.stocks_owned
			if StocksOwnedString == "":
				StocksOwnedDict = {}
			else:
				StocksOwnedDict = eval(StocksOwnedString)

			print request.session["price"]
			print StocksOwnedDict
			if(BuyStocksCountInteger > 0):
				print "Buying stocks"
				(StocksOwnedDict,user_balance) = BuyStock(StocksOwnedDict,symbol,BuyStocksCountInteger,user_balance)
				StocksOwnedString = repr(StocksOwnedDict)
				current_user.stocks_owned = StocksOwnedString
				current_user.balance = user_balance
				current_user.save()


			if(SellStocksCountInteger > 0):
				print "Selling stocks"
				StocksOwnedDict,user_balance = SellStock(StocksOwnedDict,symbol,SellStocksCountInteger,user_balance)
				StocksOwnedString = repr(StocksOwnedDict)
				current_user.stocks_owned = StocksOwnedString
				current_user.balance = user_balance
				current_user.save()

	# print form
	displayed_keys = ['Ask','YearLow','DividendShare','ChangeFromFiftydayMovingAverage','FiftydayMovingAverage','DividendYield','ChangeFromYearLow','ChangeFromYearHigh','AverageDailyVolume']
	company_details = {key:temp[key] for key in displayed_keys}
	return render_to_response('company.html',{'user':ThisUser,'company_details':company_details,'stock_form':form}, RequestContext(request))



def account_view(request):
	ThisUser = request.user
	current_user = UserProfile.objects.get(user = ThisUser)
	user_balance = current_user.balance 
	StocksOwnedString = current_user.stocks_owned
	if StocksOwnedString == "":
		StocksOwnedDict = {}
	else:
		StocksOwnedDict = eval(StocksOwnedString)
	return render_to_response('account.html',{'user':ThisUser,'user_balance':user_balance,'stocks_owned':StocksOwnedDict}, RequestContext(request))
