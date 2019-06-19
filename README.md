# Lookup on Company's Name from a query on https://macaddress.io/ API

__Requirement__
- API Key is required in order to achieve API query on macaddress lookup API. Click [here](https://macaddress.io/signup) to sign up for API Key creation. This Key would be required for this script.
- MAC Address is required for the search
- Install python when running the script on a Linux system. ``yum install -y python``
- Install docker when running the script as a container on a Linux system. `yum install docker -y`

### Steps ###
- Clone the repository `git clone https://github.com/josfem004/maclookup_apy.git`
- `cd maclookup_apy`
- To run the script 
  `chmod +x api.py && python -i api.py` 
  Enter the Value of the MAC Address and the API Key
- To run as a container
  - Build docker images by running `docker build -t api/maclookup` which will run against the dockerfile
  - `docker run -it api/maclookup`
  Enter the Value of the MAC Address and the API Key
