user_email = "abc@gail.com"

email_services = ["hotmail", "gmail", "yahoo"]
email_contains_service = any(email_service in user_email for email_service in email_services)

print(email_contains_service)