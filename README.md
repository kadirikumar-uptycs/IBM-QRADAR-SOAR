# Threat Analysis with Uptycs

## Necessary Packages

- resilient
- resilient_circuits
- resilient_lib
- resilient_sdk

## How to run

- Enable python virtual environment (using command => ``.venv/Scripts/activate``)
- Install all the necessary packages using pip
- Go to the ``C:\Users\USER\.resilient`` folder and edit the app.config file in that folder with the appropriate SOAR intance details
- Change working directory to [threat_analysis_with_uptycs](https://github.com/kadirikumar-uptycs/QRADAR-SOAR-V1/tree/main/threat_analysis_with_uptycs)
- Run ``resilient-circuits config -c``, then edit the ``threat_analysis_with_uptycs`` section in ``C:\Users\USER\.resilient\app.config`` with appropriate values
- Run ``pip install -e .``
- Run ``resilient-circuits run``

## Steps to build App from scratch

#### Create Template with below command

```
  resilient-sdk codegen -p 
```

#### Important files/folders list in the template

- `<app-name>`/components/func_`<function-name>`.py - The task that needs to be performed by the function is written in this file.
- `<app-name>`/util/config.py - We can define config data related to the app that needs to be defined in the app.config file. This config data can be referenced by the app during runtime.
- `<app-name>`util/customize.py- Contains the summary of functions, destinations, fields, etc. associated with the app. Automatically generated.
- `<app-name>`util/data/export.res - Contains the application's entities (functions, workflows, fields, destinations, etc.) definitions. The SOAR instance refers to this file to understand what functions, fields, etc. the app needs and creates those on the SOAR instance during the installation of app.
- apikey_permissions.txt - Defines the permissions required by the app.
- setup.py - defines the name of the app, version, description, etc., and requirements and dependencies.
- Readme.md - Markdown readme file describing the app and its usage.

##### Once the setup is complete, install the application using pip in editable mode by being in the folder where setup.py is present and running the command:

```
pip3 install -e .
```

##### Validate if the app is successfully installed, run the following command. The app and its functions will be listed if the installation is successful.

```
resilient-circuits list
```

##### We can run resilient circuits and test the connection with the CP4S instance. Once the resilient-circuits is run, it will listen to the destination configured for the app and any request in the destination is passed to the app for processing and the results are passed back to the destination. To run resilient-circuits, enter the following command:

```
resilient-circuits run
```

##### If the connection is successful, we can see the following message:

```
2024-04-02 15:33:39,077 INFO [stomp_component] [resilient_circuits] Client HB: 0  Server HB: 15000
2024-04-02 15:33:39,078 INFO [stomp_component] [resilient_circuits] No Client heartbeats will be sent
2024-04-02 15:33:39,078 INFO [stomp_component] [resilient_circuits] Requested heartbeats from server.
2024-04-02 15:33:39,081 INFO [actions_component] [resilient_circuits] STOMP connected.
2024-04-02 15:33:39,184 INFO [actions_component] [resilient_circuits] resilient-circuits has started successfully and is now running...
2024-04-02 15:33:39,186 INFO [actions_component] [resilient_circuits] Subscribe to message destination 'fn_uptycs_api'
2024-04-02 15:33:39,188 INFO [stomp_component] [resilient_circuits] Subscribe to message destination actions.201.fn_uptycs_api
```

##### If we want to include any other function in the app we add it by running the following command. This will create the templates for the new functions.

```
resilient-sdk --reload -p <package-name> -f <list of functions>
```

### Packaging

Package the app (Create the a app package which can be installed on SOAR instances), by running the following command (be in the app home directory before running the command):

```
resilient-sdk package -p .
```

### Validation

We can also validate the package for quality and security issues by adding the **"--validate"** flag to the above command. This flag is needed when are submitting the app for publishing it on IBM app store as community version.

We can run the validation step separately as well by running the command:

```
resilient-sdk validate -p <package-name>
```
