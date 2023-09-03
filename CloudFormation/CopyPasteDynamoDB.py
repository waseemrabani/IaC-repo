import boto3

def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb')

    # Define the source and destination table names
    source_table_name = 'SourceTable'
    destination_table_name = 'DestinationTable'

    # Use the DynamoDB scan method to retrieve all items from the source table
    source_table_items = dynamodb.scan(TableName=source_table_name)

    # Iterate over the items and put each one into the destination table
    for item in source_table_items['Items']:
        dynamodb.put_item(TableName=destination_table_name, Item=item)
