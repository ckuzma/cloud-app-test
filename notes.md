- DuckDuckGo search for `aws python app`, first link involved Django, second was a full tutorial, third was developer center
    - 4th link: https://blog.seamlesscloud.io/2020/07/how-to-deploy-a-python-flask-app-to-aws-elastic-beanstalk/
- Upon attempting to sign in to AWS console, was greeted with account suspended page
    - On the payment page, found no outstanding dues
    - Attempted to re-sign-up via the AWS free tier link
        - https://aws.amazon.com/free/
        - Waited for email to arrive to unlock account
- **BLOCKED**
- Day 2 @ 10:42 clicked on Contact Us when no email arrived
    - Heather:
        ```
        Hey Christopher! Wish i could help here, but this is something our AWS Accounts and Billings team will have to help you with. This may be due to inactivity of your account, it suspends after 90 days.
        ```
    - Was given link to contact Accounts and Billing team
- Created a new ticket/case and chose the chat option with AWS to resolve it @ 10:50
    - Apparently my account was closed in October 2019 via self-service, thus unable to re-open (10:53am)
- 10/12/2020 @ 15:54 started again
- 15:57 zipped up files in project directory, uploaded, clicked create
- 16:01, marked as successfully deployed
    - Not sure why health marked as severe
    - Would not open, 502 bad gateway
- 16:06, found Python boiler plate
    - https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tutorials.html
    - This time, compressed the root folder of the project into zip and uploaded @ 16:07
    