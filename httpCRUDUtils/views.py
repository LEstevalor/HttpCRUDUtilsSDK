from django.http import HttpResponse, JsonResponse
from django.views import View
from httpCRUDUtils.client import HttpCRUDUtils


class RequestHandler(View):
    def get(self, request):
        page_info = HttpCRUDUtils().base_get("http://www.baidu.com/")
        if page_info:
            return HttpResponse(page_info)
        else:
            return HttpResponse("无法获取百度页面信息。", status=500)

    def post(self, request):
        # 在这里处理POST请求，示例中仅返回一个JSON响应
        return JsonResponse({"message": "POST request received"})

    def put(self, request):
        # 在这里处理PUT请求，示例中仅返回一个JSON响应
        return JsonResponse({"message": "PUT request received"})
