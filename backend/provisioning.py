import os
import requests

from dotenv import load_dotenv

load_dotenv()


# --------------------------------
# Jira
# --------------------------------

def create_jira_user(user):

    return {
        "status": "success",
        "external_user_id": f"jira-{user['email']}",
        "message": "Jira provisioning simulated successfully"
    }

# --------------------------------
# GitHub
# --------------------------------

def create_github_user(user):

    token = os.getenv("GITHUB_TOKEN")

    if not token:

        return {
            "status": "skipped",
            "message": "GitHub configuration missing"
        }

    # GitHub does not generally allow arbitrary
    # user accounts to be created through a normal
    # public API.
    #
    # This function therefore represents the place
    # where your GitHub organization/invitation logic
    # should be implemented.

    return {
        "status": "success",
        "message": (
            "GitHub provisioning workflow "
            "can be implemented here"
        )
    }


# --------------------------------
# Slack
# --------------------------------

def create_slack_user(user):

    return {
        "status": "success",
        "message": (
            "Slack provisioning workflow "
            "can be implemented here"
        )
    }


# --------------------------------
# Main provisioning function
# --------------------------------

def provision_user(user, applications):

    results = {}

    for application in applications:

        application = application.lower()

        if application == "jira":

            results["jira"] = create_jira_user(user)

        elif application == "github":

            results["github"] = create_github_user(user)

        elif application == "slack":

            results["slack"] = create_slack_user(user)

        else:

            results[application] = {
                "status": "failed",
                "message": "Unsupported application"
            }

    return results