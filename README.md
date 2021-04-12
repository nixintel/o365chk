### o365chk.py

Simple Python script to check if there is an Office365 instance linked to a particular domain.

There are three possible results:

Unknown = No O365 instance for that domain
Federated = O365 is federated
Managed = O365 is managed directly by Microsoft

### Installation and Usage

``````
$ git clone https://github.com/nixintel/o365chk

$ pip install -r requirements.txt

$ python3 o365chk.py -d example.com

``````

### Example Output

``````
$ python3 o365chk.py -d bbc.co.uk

This domain is Federated
{
    "AuthNForwardType": 1,
    "AuthURL": "https://gateway.id.tools.bbc.co.uk/eiam/WSFederationServlet/metaAlias/wsidp2?username=username%40bbc.co.uk&wa=wsignin1.0&wtrealm=urn%3afederation%3aMicrosoftOnline&wctx=",
    "CloudInstanceIssuerUri": "urn:federation:MicrosoftOnline",
    "CloudInstanceName": "microsoftonline.com",
    "DomainName": "bbc.co.uk",
    "FederationBrandName": "BBC",
    "FederationGlobalVersion": -1,
    "Login": "username@bbc.co.uk",
    "NameSpaceType": "Federated",
    "State": 3,
    "UserState": 2
``````

###Credits

I had the idea for this after reading this excellent article by Mike Bond: https://bond-o.medium.com/microsoft-office-365-enumeration-58f9b5ba21c8
