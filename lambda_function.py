import boto3
import json
 
ses = boto3.client('ses', region_name='us-east-1')
 
def lambda_handler(event, context):
    print("Event received:", json.dumps(event))  # Debugging
 
    try:
        # Handle both proxy and non-proxy integration
        raw_body = event.get("body")
        if raw_body:
            body = json.loads(raw_body)
        else:
            body = event
 
        response = ses.send_email(
            Source='nabengyeflorence51@gmail.com',
            Destination={'ToAddresses': ['n.yelbert@gmail.com']},
            Message={
                'Subject': {
                    'Data': f"Form successfully submitted from {body.get('name', '')}"
                },
                'Body': {
                    'Text': {
                        'Data': f"You have a new message:\n\n"
                                f"Name: {body.get('name', '')}\n"
                                f"Email: {body.get('email', '')}\n"
                                f"Message: {body.get('message', '')}"
                    }
                }
            }
        )
 
        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"success": True, "message": "Email sent successfully!"})
        }
 
    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"success": False, "error": str(e)})
        }