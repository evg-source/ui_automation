import os
import logging

# Path to Chromedriver executable
chromedriver_path = ""
if len(chromedriver_path) == 0:
    chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')

# Webpage URL
scale_page_url = "http://ec2-54-208-152-154.compute-1.amazonaws.com/"

debug_level = logging.INFO
