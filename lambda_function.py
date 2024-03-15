import json
import boto3

def lambda_handler(event, context):
    # Extract filtered booking records from the EventBridge event
    filtered_bookings = event.get('filtered_bookings', [])
    
    # Write filtered booking records to S3 bucket
    s3_bucket_name = 'airbnb-booking-records-rahesh'
    s3_key = 'filtered_bookings.json'
    s3_object = {'filtered_bookings': filtered_bookings}
    
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    # Write data to S3 bucket
    try:
        response = s3_client.put_object(
            Bucket=s3_bucket_name,
            Key=s3_key,
            Body=json.dumps(s3_object)
        )
        print("Filtered bookings written to S3 successfully")
        return {
            'statusCode': 200,
            'body': 'Filtered bookings written to S3 successfully'
        }
    except Exception as e:
        print(f"Error writing filtered bookings to S3: {e}")
        return {
            'statusCode': 500,
            'body': f'Error writing filtered bookings to S3: {e}'
        }
