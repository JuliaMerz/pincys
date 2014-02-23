from boto.mturk.connection import MTurkConnection
from keys import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

HOST = 'mechanicalturk.sandbox.amazonaws.com'

mtc = MTurkConnection(aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      host=HOST)
                      
print mtc.get_account_balance()