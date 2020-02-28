# VPN Checker service.


## How to install

 1. Clone this repository into your local system.
 2. Start a new python virtual environment:
	```bash
	$: sudo apt install virtualenv
    $: virtualenv -p python3 vpn_checker
    ```
 3. Activate the new virtual environment:
	```bash
	$: source vpn_checker/bin/activate
	```
 4. Move into the repository source code.
 5. Install the python requirements for this project to work:
	```bash
	(vpn_checker)$: pip install -r requirements.txt
	```
 6. Now you can run the VPN Checker service.
	```bash
	(vpn_checker)$: python main.py
	```

## Creating a Linux service daemon using Systemd

 1. Create a `vpn_checker.service` file into the **/etc/systemd/system** folder with the following content:
	```bash
	[Unit]
	Description=VPN Checker Service
	After=network.target
	StartLimitIntervalSec=0

	[Service]
	Type=simple
	Restart=always
	RestartSec=1
	User=<TYPE YOUR USERNAME HERE>
	Environment="DISPLAY=:0.0"
	Environment="DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus"
	ExecStart=$VIRTUALENV_PATH/bin/python $SOURCES_PATH/main.py

	[Install]
	WantedBy=multi-user.target
	```
	**NOTE:** You need to change the values for the `DISPLAY` and `DBUS_SESSION_BUS_ADDRESS` environment variables. Normally if you execute `echo $DISPLAY` and `echo $DBUS_SESSION_BUS_ADDRESS` you will be able to get this values and replace them.
	Also you need to replace the `VIRTUALENV_PATH` value to match the correct python virtual environment directory path in your system and the `SOURCES_PATH` to match the repository sources directory path also in your system :).

 2. With the previous step in place, now we can `enable` this new service into the **systemd** environment:
	```bash
	$: sudo systemctl enable vpn_checker.service
	```
 3. And finally we can `start` the `vpn_checker` service:
	```bash
	$: sudo systemctl start vpn_checker
	```
**NOTE**: Now, every time you start your computer, `systemd` will automatically start the `vpn_checker` service. So, if you want to stop the service manually, then you need to run **`sudo systemctl stop vpn_checker`**.

