# Robot-Bartender
The Robot Bartender is a project created to have a deeper understanding of lower level networking fundamentals, while also using this as an excuse to understand Android development, and Android networking on a deeper level. 

The Robotic Bartender runs a custom made server developed with Python, and interfaces with Android devices running on Java. An issue found during the development of the project shows that Multicast requests are not able to be received on newer Android versions, even with correct permission settings, forcing a manual connection via direct IP, or the use of POST requests sent via a webserver effectively acting as our API. 

