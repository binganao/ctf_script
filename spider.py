# 简单的爬虫脚本，可以稍作修改用于SQL盲注、爆破密码和FUZZ
import requests
import re

from requests.api import get

target_url = ""
headers = {
  # "X-Forwarded-For": "127.0.0.1",
  # "Cookie": "", 
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15", 
  "Accept": "*/*", 
}

# 最简单的爬虫 可以配合多线程使用
def run_spider(param): 
  r = requests.get(target_url, headers=headers)
  # r = requests.post(target_url, headers=headers)
  print(r.text)
  html = r.text
  # html = r.content.decode("gb2312")
  get_ness_text = re.findall(r'', html)
  print(get_ness_text)
  if(get_ness_text == ''):
    # do something
    pass
  else:
    # do something
    pass
  
if __name__ == '__main__':
  run_spider('parm')