import pandas as pd
import os
import urllib
import csv
import matplotlib.pyplot as plt


datasets[0].head(n=5)

data = datasets[0] # assign SQL query results to the data variable

data = data.fillna('') # replace missing values with strings for easier text processing
    
