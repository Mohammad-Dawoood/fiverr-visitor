#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import requests
from datetime import datetime

links = ["https://www.fiverr.com/m_dawood_irfan/do-data-processing-data-cleaning-and-data-analysis?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=7yqyg71",
                 "https://www.fiverr.com/m_dawood_irfan/do-python-web-scrapping-data-scrapping-survey-automation?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=0bzbr8q",
                 "https://www.fiverr.com/m_dawood_irfan/automate-your-daily-data-related-tasks?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=e6y6qrr",
                 "https://www.fiverr.com/m_dawood_irfan/automate-google-sheet-with-formulas?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=pd6930l"]
import time
from DrissionPage import WebPage, ChromiumOptions
o = 1
while True:
    try:
        for i in links:
            co = ChromiumOptions()
            co.headless(True)
            co.mute(True)
            co.incognito(True)
            page = WebPage(chromium_options=co, mode='d')
            time.sleep(5)
            # page = MixPage()
            page.get(i)
            for i in range(1,15):
                page.actions.scroll(delta_y=300)
                time.sleep(1)
            time.sleep(5)
            page.quit(del_data=True)
        print(f'Sesion {o} Run Sucessfully.')
        time.sleep(20)
        o+=1
    except Exception as e:
        print(e)
        print("An Error Occured.\n")
        print('Retrying...\n')

# In[ ]:




