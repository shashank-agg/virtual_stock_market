import json
import yahoo.yql
from pprint import pprint

def GetAllStocks ():
  response = yahoo.yql.YQLQuery().execute("select * from yahoo.finance.quote where symbol in (select company.symbol from yahoo.finance.industry where id=821)")
  # 821 corresponds to the industry 'Application Software'.Cannot query by name since only id can be used in where
  if 'error' in response or ('query' not in response) or ('results' not in response['query']):
    return ''
  return response['query']['results']['quote']

def GetCompanyDetails (symbol):
  query = "select * from yahoo.finance.quotes where symbol = '"+symbol + "'"
  response = yahoo.yql.YQLQuery().execute(query)
  if 'error' in response or ('query' not in response) or ('results' not in response['query']):
    return ''
  
  return response['query']['results']['quote']


if __name__== '__main__':
     pprint(GetAllStocks())
