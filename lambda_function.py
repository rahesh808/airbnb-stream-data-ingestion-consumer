import json
import boto3

def lambda_handler(event, context):
    # Check if the event is an SQS event
        # Extract the body from the first record
        body = json.loads(event[0]['body'])
        
        # Convert the body to a JSON string
        body_json = json.dumps(body)
        
        booking_data = json.loads(body_json)
        del booking_data['duration']
        # Access the bookingId
        booking_id = booking_data['bookingId']
        print(booking_data)
        # Store the JSON string in an S3 bucket
        s3_bucket_name = 'airbnb-booking-records-rahesh'
        s3_key = f'{booking_id}.json' 
        s3_client = boto3.client('s3')
        s3_client.put_object(
            Body=booking_data,
            Bucket=s3_bucket_name,
            Key=s3_key
        )
        print("uploaded to s3")
        
        return {
            'statusCode': 200,
            'body': 'Successfully stored booking data in S3'
        }
   
