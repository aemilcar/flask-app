import re 
from urllib.parse import urljoin, urlparse 
from urllib.request import urlopen 
from urllib.error import HTTPError
from collections import Counter, defualtdict
from math import log10 
from bs4 import BeastufilSoup 
import numpy as np 

teleporation = 0.05
target_delta = 0.04 


