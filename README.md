# Testable-Calibration-EBT3-UI
The EBT3 films are a very popular and usefull dosimeter for quality control in radiotherapy (RT).

Here is a try of an UI for making the calibration curve of the EBT3 sets faster and in a principle easier if your hospital doesnt count with a  dedicated software for it.

The neccesary libraries to run the UI are:
- PyQt5
- numpy
- math
- prettytable
- datatime
Is also important to know that to run the python file, is neccessary that the .ui file is in the same folder.

# Important disclaimers
1- This UI was designed to be used in the Hospital Universitario of the Universidad Autónoma de Nuevo León, but its IMPORTANT to know that is still in testing for problems in the results, so take that in account to its use and if have something to say I'm open to feedback.

2- At first is logical, but the file browser of the UI only recognize the .tif images.

----

# UI main window:
![MAIN WINDOW](https://user-images.githubusercontent.com/125628193/222052124-6d2211f3-2156-475a-9e37-4d1fef57c916.png)

In the main window we have four important areas, they're also numbered in the order that should be used for making a calibration curve for the first time (although we actually use the first and second areas practicaly at the same time) and we are gonna explain them in that order.
----

# PTR scans uploader 
In this section we're gonna upload the scans of the PTR's that we threat with radiation, to do that we need to click in the green squares. Before we star explaining the process is important to know that the first square or 'PELÍCULA SIN IRRADIAR' is for the EBT3 film that wasnt irradiated and thats the reason because have a box of 0 cGy; taking this in account is crucial for the good functioning of the UI, or at least to get a good calibration curve.

## The steps for using the uploader section:
- Click in a green square and select the .tif image that represents your EBT3 film. This will open the file browser.
![Browser](https://user-images.githubusercontent.com/125628193/222057061-c888d189-e4c4-437a-a4ff-7b9c8998c6a0.png)

- Select the image in the browser and then you will have this:
![pending](https://user-images.githubusercontent.com/125628193/222057402-12a858ef-1722-49c2-9321-92301a7ce30e.png)
  Here we can see two things:
  * The square now is orange, this is because we don't the program doesn't have save information of that image yet

