import requests
import json
import argparse


def make_requests(target):

    url = 'https://login.microsoftonline.com/getuserrealm.srf?login=username@'+str(target)+'&json=1'

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Uh-oh: Something Bad Happened", err)
        raise SystemExit(e)

    r = r.json()

    return r


def get_status(response_json):

    x = json.dumps(response_json)

    x = json.loads(x)

    status = x['NameSpaceType']

    if status == 'Managed':
        print('This domain is Managed')
    elif status == 'Federated':
        print('This domain is Federated')
    elif status == 'Unknown':
        print('No O365 service could be identified for this domain, or it was entered incorrectly.')
    else:
        print('No O365 status could be found, or there was an error')

    return x


def main():

    parser = argparse.ArgumentParser(description='Checks to see if an O365 instance is associated with a domain.')
    parser.add_argument('-d', '--domain', help='Specifies the domain to be checked', required=True)
    args = parser.parse_args()

    domain = args.domain

    data = make_requests(domain)

    result = get_status(data)

    print(json.dumps(result, indent=4, sort_keys=True))

main()