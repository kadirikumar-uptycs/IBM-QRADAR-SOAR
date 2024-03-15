# Threat Analysis with Uptycs

## Necessary Packages
- resilient
- resilient_circuits
- resilient_lib
- resilient_sdk

## How to run
- Enable python virtual environment (using command => ```.venv/Scripts/activate```)
- Install all the necessary packages using pip
- Go to the ```C:\Users\USER\.resilient``` folder and edit the app.config file in that folder with the appropriate SOAR intance details
- Change working directory to [threat_analysis_with_uptycs](https://github.com/kadirikumar-uptycs/QRADAR-SOAR-V1/tree/main/threat_analysis_with_uptycs)
- Run ```resilient-circuits config -c```, then edit the ```threat_analysis_with_uptycs``` section in ```C:\Users\USER\.resilient\app.config``` with appropriate values
- Run ```pip install -e .```
- Run ```resilient-circuits run```
