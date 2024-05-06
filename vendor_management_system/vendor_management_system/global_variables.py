from rest_framework.response import Response
from rest_framework import status

def generic_json_response(success = True, status_code = 200, message = "", error = {}, result = {}):
    '''
        Generic common function to return the response
    '''
    response_body = {"success": success,
                     "status_code": status_code,
                     "message": message,
                     "result":result,
                     "error": error}
    
    return Response(response_body, status = status_code)