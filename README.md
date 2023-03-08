# BUTTPlugin-for-JRiver-Media-Center-using-Python
Update song name from file for BUTT using Python, grabbing information from JRiver Media Center server .xml file.

This plugin requires the "requests" python include.  Detailed instructions to download found here:
http://docs.python-requests.org/en/master/
http://docs.python-requests.org/en/master/user/install/#install

This program originally developed on python 3.6

Steps for use:
1. To run the program, install the requests library for Python, and install Python 3.6 (other versions will likely work as well, so long as they support the requests library)
2. Make sure BUTTInfo.txt and the GetInfo.py are in the same folder. (Otherwise you'll need to change the pointer on file opening to the proper location)
3. Open up BUTT and begin streaming as normal.  Under the STREAM tab of settings, browse and select the BUTTInfo.txt file. Make sure the checkbox for ACTIVATE is checked.
4. Double click on GetInfo.py and the program will begin running.
5. You should have something that looks like this: https://i.imgur.com/vvSFLux.png
6. Congrats! Assuming BUTT was working well before, you should now have Song & Artist info attached to your stream and displaying.

The information should be displayed like this https://i.imgur.com/5k3vzxQ.png

Feel free to message me for comments, questions, and concerns, no matter how dumb you think it may be.
