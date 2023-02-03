
from autoscraper import AutoScraper

amazon_url='https://www.amazon.in/s?k=bags'

wanted_list=['Skybags Brat Black 46 Cms Casual Backpack','₹669','3,368',]

scrap=AutoScraper()
results=scrap.build(amazon_url,wanted_list)

results

scrap.get_result_similar(amazon_url,grouped=True)

scrap.set_rule_aliases({'rule_5l6a':'Title','rule_hmod':'Price','rule_dmr5':'Rating'})
scrap.keep_rules(['rule_5l6a','rule_hmod','rule_dmr5'])
scrap.save('amazon-search')

data=scrap.get_result_similar("https://www.amazon.in/s?k=bags",group_by_alias=True)

data['Title']

data

data["Price"]=data["Price"][:16]

import pandas as pd
len(data["Rating"])

d=pd.DataFrame(data)

d.to_csv('file_1.csv')

