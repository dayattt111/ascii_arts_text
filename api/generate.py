import json

def handler(request):
    try:
        body = request.get_json()
        text = body.get("text", "")

        # contoh proses: ubah ke ASCII sederhana
        ascii_art = "\n".join([ " ".join(list(line)) for line in text.split("\n") ])

        return {
            "statusCode": 200,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps({"ascii": ascii_art})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
