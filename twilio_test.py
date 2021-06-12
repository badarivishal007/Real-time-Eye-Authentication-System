from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC492c24a66b19e4d56fef97e07cb50c2e"
auth_token = "caf27623fe6b28a9409587a16f3dbf03"

client = Client(account_sid, auth_token)



client.api.account.messages.create(
    to="+91-8867037352",
    from_="+15615134536" ,  #+1 210-762-4855"#14804852511
    body="Detected")
