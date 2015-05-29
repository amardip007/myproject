__author__ = 'vicky-pc'

from django.shortcuts import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from lxml import etree
from ystockquote import get_historical_prices
from lxml import html
import urllib2
import datetime
import urllib

import time
import csv

def first_page(request):
    return render_to_response('myapp/home1.html')

def yahoo_finanace(request):
#     start_date = '2015-01-01'
    next_date = datetime.datetime.now().date()
    next_date_year = next_date.year
    next_date_month = next_date.month
    if next_date_month >= 1 and next_date_month <=9:
        next_date_month = str(0) + str(next_date_month)
    next_date_day = next_date.day 
    if next_date_day >= 1 and next_date_day <= 9:
        next_date_day = str(0) + str(next_date_day)
    next_date = str(next_date_year) + '-' + str(next_date_month) + '-' + str(next_date_day)
    
    
    total_yhoo_data = []
    if request.method == 'GET':
        ticker_name = request.GET.get('text_co')
        ticker_name = ticker_name.upper()
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if not end_date:
            next_date = next_date
        else:
            next_date = end_date
        try: 
            data = get_historical_prices(''.join(ticker_name),start_date,next_date)
           
        
            for each_key in sorted(data.keys(),key=str):
                
                each_yhoo_row = {}
                nxt_dict = data[each_key]
                ticker = ''.join(ticker_name)
                updatin_date = each_key
                updatin_date = datetime.datetime.strptime(updatin_date,'%Y-%m-%d')
               
                open = round(float(nxt_dict['Open']),2)
                high =round(float(nxt_dict['High']),2)
                low = round(float(nxt_dict['Low']),2)
                close = round(float(nxt_dict['Close']),2)
                volume = nxt_dict['Volume']
                
                each_yhoo_row =  {'fin_date':str(each_key),'open':open,'high':high,'low':low,'close':close,'volume':volume}
                total_yhoo_data.append(each_yhoo_row)
    #                 insert_data = "insert into cmpdata_2015(ticker,date,open,high,low,close,volume) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    #                 VALUES = (ticker,updatin_date,open,high,low,close,volume)
    #                 cursor.execute(insert_data,VALUES)
    #                 connection.commit()
                print "Successfully saved", ticker
       
        
        
            context_dict = {'yhoo_data':total_yhoo_data}
        except:
            context_dict = {}
    
    return render_to_response('myapp/home1.html', context_dict,context_instance=RequestContext(request))

