import logging

from httpCRUDUtils.client import HttpCRUDUtils

logger = logging.getLogger(__name__)


http_util = HttpCRUDUtils()

r = http_util.base_get(base_path="http://www.baidu.com/")
logger.info(r)  # <Response [200]>
logger.info(type(r))  # <class 'requests.models.Response'>
logger.info(r.status_code)  # 200

print(r)  # <Response [200]>
print(type(r))  # <class 'requests.models.Response'>
print(r.status_code)  # 200
print(r.content)   # <!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;...

# # 不能在children没有赋值的情况下直接append，KeyError: 'children'
# metric_list = []
# dict_info = {"id": 1, "label": 2, "children": []}
# dict_info["children"].append({"id": 2, "label": 2})
# metric_list.append(dict_info)
