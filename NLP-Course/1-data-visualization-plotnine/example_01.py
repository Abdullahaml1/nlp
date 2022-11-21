import pandas as pd
from plotnine import *

weather=pd.read_csv("https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv")

(ggplot(weather,aes('Month', 'Tmax'))
  + geom_line()
)
