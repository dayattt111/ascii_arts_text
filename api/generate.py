import json

# def handler(request):
#     return {
#         "statusCode": 200,
#         "headers": {"Content-Type": "application/json"},
#         "body": json.dumps({"message": "Python API is working!"})
#     }
def handler(request):
    return {
        "status": 200,
        "body": "API Python Berhasil"
    }
