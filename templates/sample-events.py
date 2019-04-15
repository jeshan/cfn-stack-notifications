event = {'version': '0', 'id': 'f34478bd-ca7c-747d-97a0-f817a99b6b7f', 'detail-type': 'AWS API Call via CloudTrail',
         'source': 'aws.cloudformation', 'account': '406883123076', 'time': '2019-04-15T06:06:00Z',
         'region': 'us-east-1',
         'resources': [], 'detail': {'eventVersion': '1.05',
                                     'userIdentity': {'type': 'IAMUser', 'principalId': 'AIDAIQGNQ3ENV7EEEKXZG',
                                                      'arn': 'arn:aws:iam::406883123076:user/jeshan',
                                                      'accountId': '406883123076',
                                                      'accessKeyId': 'AKIAV5PA7X6CO5TSI26Q',
                                                      'userName': 'jeshan'}, 'eventTime': '2019-04-15T06:06:00Z',
                                     'eventSource': 'cloudformation.amazonaws.com', 'eventName': 'UpdateStack',
                                     'awsRegion': 'us-east-1', 'sourceIPAddress': '41.136.225.217',
                                     'userAgent': 'Boto3/1.9.109 Python/2.7.12 Linux/4.15.0-43-generic Botocore/1.12.109',
                                     'requestParameters': {'notificationARNs': [], 'parameters': [],
                                                           'stackName': 'cfn-stack-notifications-dev-main',
                                                           'capabilities': ['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM',
                                                                            'CAPABILITY_AUTO_EXPAND']},
                                     'responseElements': {
                                         'stackId': 'arn:aws:cloudformation:us-east-1:406883123076:stack/cfn-stack-notifications-dev-main/0d005050-5f44-11e9-8f29-0a79b0f3a14a'},
                                     'requestID': '8aca772d-5f44-11e9-b3d4-d5bf0eb3faf8',
                                     'eventID': 'b1f5ef28-e752-470f-b87b-a91ca0e98333', 'eventType': 'AwsApiCall'}}

stack_name = event['detail']['requestParameters']['stackName']
stack_id = event['detail']['responseElements']['stackId']

topics = event['detail']['requestParameters']['notificationARNs']

event = {'version': '0', 'id': 'fb4d73c7-369a-11a5-6b07-b57bc2be12f0', 'detail-type': 'AWS API Call via CloudTrail',
         'source': 'aws.cloudformation', 'account': '406883123076', 'time': '2019-04-15T06:44:59Z',
         'region': 'us-east-1', 'resources': [], 'detail': {'eventVersion': '1.05', 'userIdentity': {'type': 'IAMUser',
                                                                                                     'principalId': 'AIDAIQGNQ3ENV7EEEKXZG',
                                                                                                     'arn': 'arn:aws:iam::406883123076:user/jeshan',
                                                                                                     'accountId': '406883123076',
                                                                                                     'accessKeyId': 'AKIAV5PA7X6CO5TSI26Q',
                                                                                                     'userName': 'jeshan'},
                                                            'eventTime': '2019-04-15T06:44:59Z',
                                                            'eventSource': 'cloudformation.amazonaws.com',
                                                            'eventName': 'UpdateStack', 'awsRegion': 'us-east-1',
                                                            'sourceIPAddress': '41.136.225.217',
                                                            'userAgent': 'Boto3/1.9.109 Python/2.7.12 Linux/4.15.0-43-generic Botocore/1.12.109',
                                                            'requestParameters': {'notificationARNs': [],
                                                                                  'parameters': [
                                                                                      {'parameterKey': 'Email'}],
                                                                                  'stackName': 'cfn-stack-notifications-dev-main',
                                                                                  'capabilities': ['CAPABILITY_IAM',
                                                                                                   'CAPABILITY_NAMED_IAM',
                                                                                                   'CAPABILITY_AUTO_EXPAND']},
                                                            'responseElements': {
                                                                'stackId': 'arn:aws:cloudformation:us-east-1:406883123076:stack/cfn-stack-notifications-dev-main/0d005050-5f44-11e9-8f29-0a79b0f3a14a'},
                                                            'requestID': 'fd289f8e-5f49-11e9-adaa-7fae8cc86a32',
                                                            'eventID': '3c7825ee-496e-4303-8aba-03203552a1ca',
                                                            'eventType': 'AwsApiCall'}}
