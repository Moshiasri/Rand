import pandas as pandas 
import Quandl as Quandl

df = Quandl.get('WIKI/GOOGL')

print (df.head)
