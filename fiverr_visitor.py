#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import requests
from datetime import datetime

links = [
    "https://www.fiverr.com/m_dawood_irfan/do-data-processing-data-cleaning-and-data-analysis?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=7yqyg71",
    "https://www.fiverr.com/m_dawood_irfan/do-python-web-scrapping-data-scrapping-survey-automation?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=0bzbr8q",
    "https://www.fiverr.com/m_dawood_irfan/automate-your-daily-data-related-tasks?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=e6y6qrr",
    "https://www.fiverr.com/m_dawood_irfan/automate-google-sheet-with-formulas?utm_campaign=gigs_show&utm_medium=shared&utm_source=copy_link&utm_term=pd6930l"
]

def visit_page(url, session_num, link_num):
    """Visit a page using requests library"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        # Make request to the page
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200:
            print(f"  ✓ Link {link_num}: Success (Status: {response.status_code})")
            return True
        else:
            print(f"  ✗ Link {link_num}: Failed (Status: {response.status_code})")
            return False

    except requests.exceptions.RequestException as e:
        print(f"  ✗ Link {link_num}: Error - {str(e)[:50]}")
        return False

def main():
    session_num = 1

    print("=== Fiverr Page Visitor Started ===")
    print(f"Starting at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    while True:
        try:
            print(f"--- Session {session_num} ---")
            print(f"Time: {datetime.now().strftime('%H:%M:%S')}")

            # Visit each link
            for idx, link in enumerate(links, 1):
                visit_page(link, session_num, idx)
                time.sleep(5)  # Wait between links

            print(f"✓ Session {session_num} completed successfully.\n")

            # Wait before next session
            time.sleep(20)
            session_num += 1

        except KeyboardInterrupt:
            print("\n\n=== Script stopped by user ===")
            break

        except Exception as e:
            print(f"✗ Error in session {session_num}: {e}")
            print("Retrying in 30 seconds...\n")
            time.sleep(30)

if __name__ == "__main__":
    main()


# In[ ]:




