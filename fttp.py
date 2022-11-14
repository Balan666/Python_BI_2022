import requests
import re

URL = "https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references"
references = requests.get(URL).text
ftps_list = re.findall(r"\sftp://.+?/.*?\s", references)
with open('ftps.txt', 'a') as output_file:
    for link in ftps_list:
        data = output_file.write(link+'\n')