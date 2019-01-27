from django.shortcuts import render

def index(request):
    return render(request, 'learning_modules/index.html')

def learning(request):
    return render(request, 'learning_modules/learning.html')

def compare(request):
    return render(request, 'learning_modules/compare.html')

def introduction(request):
    return render(request, 'learning_modules/introduction.html')

def add_compare_info(request):
    tickers = []
    pass

def whatIsInvesting(request):
    return render(request, 'learning_modules/whatIsInvesting.html')

def riskAndDiversification(request):
    return render(request, 'learning_modules/riskAndDiversification.html')

def fixedIncome(request):
    return render(request, 'learning_modules/fixedIncome.html')

def stocks(request):
    return render(request, 'learning_modules/stocks.html')

def mutualFunds(request):
    return render(request, 'learning_modules/mutualFunds.html')