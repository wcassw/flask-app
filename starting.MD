Google Ads + Linked-in Ads ~ $100/month (variable, not fixed)
HubSpot for CRM, customer funnel tracking and conversion ~ $30/month
Stripe for billing ~$0/month (I’ve decided not to monetize yet)
Quickbooks for accounting ~ $25/month
Mercury for banking ~ $0/month
Google Workspace for all communications, including voice calling ~ $18/month
Slack for automated communications (chat with us on website, deployment trigger, alerts, etc.) ~ $0/month
GitHub for source code hosting, CICD + IDE for quick changes ~ $0/month
Google Cloud for hosting ~$incredibly low /month
Google BigQuery for data warehouse ~$0/month (at current scale)
Google Looker Studio for reporting ~$0/month
Microsoft o365 to test SSO auth with MSFT ~$6/month
Startup costs: ~$400

Domains (several for testing purposes): $30
Business license + processing fees: $350

A few verification fees to establish accounts like Google Developer to publish our Chrome extension to the Chrome webstore.

IT Systems
Everything is SaaS and Single Sign On linked to Google Workspace Account (2FA with YubiKey). Google Voice for phone communications so it can ring my other phones and help screen spam phone calls. Hubspot also provides a voice number and has some fancy sales call logging built-in that I’ll explore later. Since everything is web based, I can do most of my development from a Chromebook and GitHub code spaces.
Source Code & CICD
I currently use a monorepo in GitHub with built in CI via GitHub Actions for every aspect of the business from public facing website, core go link application, to data sync and data warehouse schema management. This allows cross system changes such as updating pricing, fields, etc. with one commit. I can do this on the go from my phone in a pinch. The CICD system alerts me on Slack of build and test results so I can approve the push to production. There are components of the software written in Python and NodeJS, but this setup can easily accommodate any language if needed. I was tempted to learn Go or Rust, but that would have probably taken me an extra few days.

Data Sync
To get data from all the above systems into BigQuery, I built some simple Cloud Functions that copy data from APIs and write to BigQuery. For systems that support it I just accept a webhook feed of data changes as they happen. For deduping, I do a full sync and than run a SQL query to materialize the only the latest records:
execute_query(sql=f"SELECT * FROM `{GCP_PROJECT}.{DATASET}.{source_table_id}` QUALIFY ROW_NUMBER() OVER(PARTITION BY id ORDER BY {updated_by_field} DESC) = 1", 
              destination_table_id=f"{GCP_PROJECT}.{DATASET}.{destination_table_id}")
This happens every 15 minutes. I expect this will start to experience scale issues when I get to over 50,000 customers in the CRM or 1,000,000 users of the system due to in memory requirements. But good enough for now.

Advertising
I love LinkedIn’s targeting ability. I can target employees that once worked for Google than are now working at another engineering company with less than 1,000 employees. Here is over a million views, just from October 22nd to November 11th.

Reporting
I can see every touchpoint through the funnel through purchase which is signing up for the service. This triggers a drip campaign to nudge users to invite and grow the account. All the data is pushed in real time (or batch synced in 15m to BigQuery so I get near real time dashboards on all aspects of activity and my core business metrics.
Accounting
All receipts are automatically entered into Quickbooks and tracked to the correct GL codes, allowing continuous closing meaning I can see my exact P&L, balance sheet, and any forecasted costs coming down the pipeline. Right now I’m on a cash basis, and will likely switch to accrual if this turns into anything meaningful.

What is next?
I’m tempted to create a “virtual sales staff” essentially building a SaaS software — very light CRM and sales tracking to allow others to become virtual sales staff and pay anybody that wants to sell my services 20% of first year revenue and 5% of year two revenue. If they sell a customer with 10,000 employees, they would get a check for $20,000 for year one and $5,000 in year two. I think this would unlock a very interesting business model and allow meaningful freelance revenue for some enterprising individuals. Please let me know if you are interested!
I’ll post later about the software stack, which has built in geo pinning to handle enterprise jurisdiction + global HA, but here is a sneak peak on how great Google is when you embrace their ecosystem. I spend less than $500/month for sustained multiple QPS (queries per second).
Every deployment is automatically monitored and analyzed including performance regressions:



----- codespaces
https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-python-project-for-codespaces

{
	"name": "Python 3",
	"build": {
		"dockerfile": "Dockerfile",
		"context": "..",
		"args": {
			// Update 'VARIANT' to pick a Python version: 3, 3.6, 3.7, 3.8, 3.9
			"VARIANT": "3",
			// Options
			"INSTALL_NODE": "true",
			"NODE_VERSION": "lts/*"
		}
	},

	// Set *default* container specific settings.json values on container create.
	"settings": {
		"terminal.integrated.shell.linux": "/bin/bash",
		"python.pythonPath": "/usr/local/bin/python",
		"python.linting.enabled": true,
		"python.linting.pylintEnabled": true,
		"python.formatting.autopep8Path": "/usr/local/py-utils/bin/autopep8",
		"python.formatting.blackPath": "/usr/local/py-utils/bin/black",
		"python.formatting.yapfPath": "/usr/local/py-utils/bin/yapf",
		"python.linting.banditPath": "/usr/local/py-utils/bin/bandit",
		"python.linting.flake8Path": "/usr/local/py-utils/bin/flake8",
		"python.linting.mypyPath": "/usr/local/py-utils/bin/mypy",
		"python.linting.pycodestylePath": "/usr/local/py-utils/bin/pycodestyle",
		"python.linting.pydocstylePath": "/usr/local/py-utils/bin/pydocstyle",
		"python.linting.pylintPath": "/usr/local/py-utils/bin/pylint"
	},

	// Add the IDs of extensions you want installed when the container is created.
	"extensions": [
		"ms-python.python"
	],

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],

	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "pip3 install --user -r requirements.txt",

	// Comment out connect as root instead. More info: https://aka.ms/vscode-remote/containers/non-root.
	"remoteUser": "vscode"
}
