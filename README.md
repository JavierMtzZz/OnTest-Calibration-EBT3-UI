# Testable-Calibration-EBT3-UI
The EBT3 films are a very popular and useful dosimeter for quality control in radiotherapy (RT).

Here is a try of an UI for making the calibration curve of the EBT3 sets faster and in a principle easier if your hospital doesn’t count with a dedicated software for it.

The necessary libraries to run the UI are:
- PyQt5
- numpy
- math
- prettytable
- datatime
Is also important to know that to run the python file, is necessary that the .ui file is in the same folder.

# Important disclaimers
1- This UI was designed to be used in the CUCC of the Hospital Universitario of the Universidad Autónoma de Nuevo León, but its IMPORTANT to know that is still in testing for problems in the results, so take that in account to its use and if have something to say I'm open to feedback.

2- At first is logical, but the file browser of the UI only recognizes the .tif images.

3- The color intensity that we extract of the tif images is in the red channel.

4- We are going to refer to the radiochromic films as PTR.

----

# UI main window:

![MAIN WINDOW](https://user-images.githubusercontent.com/125628193/222052124-6d2211f3-2156-475a-9e37-4d1fef57c916.png)

In the main window we have four important areas, they're also numbered in the order that should be used for making a calibration curve for the first time (although we actually use the first and second areas practically at the same time) and we are going to explain them in that order.

----

# 1 and 2: PTR scans uploader and image editor 

In this section we're going to upload the scans of the PTR's that we threat with radiation, to do that we need to click in the green squares. Before we star explaining the process is important to know that the first square or 'PELÍCULA SIN IRRADIAR' is for the EBT3 film that wasn’t irradiated and that’s the reason because have a box of 0 cGy; taking this in account is crucial for the good functioning of the UI, or at least to get a good calibration curve.

## The steps for using the uploader section:
- Click in a green square and select the .tif image that represents your EBT3 film. This will open the file browser.
![Browser](https://user-images.githubusercontent.com/125628193/222057061-c888d189-e4c4-437a-a4ff-7b9c8998c6a0.png)

- Select the image in the browser and then you will have this:
![pending](https://user-images.githubusercontent.com/125628193/222057402-12a858ef-1722-49c2-9321-92301a7ce30e.png)
  Here we can see two things:
  * The square now is orange; this is because the program doesn't have save information of that image yet.
  * Now there is something in the image editor.

The next step will be to use the image editor to save information of the last selected item on the square that we're using, to use the image editor we have to select a zone in the image:
![editor1](https://user-images.githubusercontent.com/125628193/222059999-b41e4e44-ab03-4e07-8430-38a3ec1fe5d4.png)

And after selecting a zone you can start to interact with the buttons below. The three buttons are respectively:
* CUT button: this will cut the zone that we selected:
![editor2](https://user-images.githubusercontent.com/125628193/222061811-9783ec04-8318-4921-8c8b-4b20b5302b7c.png)
  When we cut the image, the UI give us information in the upper right corner about the last cut that we made, we have; first the average of the intensity of color in the red channel for the zone that we selected and second the standard deviation that we suffer in the same.
* RESTABILSH button: The establish button will 
*


In this section we're gonna upload the scans of the PTR's that we threat with radiation, to do that we need to click in the green squares. Before we star explaining the process is important to know that the first square or 'PELÍCULA SIN IRRADIAR' is for the EBT3 film that wasnt irradiated and thats the reason because have a box of 0 cGy; taking this in account is crucial for the good functioning of the UI, or at least to get a good calibration curve.

## The steps for using the uploader section:
- Click in a green square and select the .tif image that represents your EBT3 film. This will open the file browser.
![Browser](https://user-images.githubusercontent.com/125628193/222057061-c888d189-e4c4-437a-a4ff-7b9c8998c6a0.png)

- Select the image in the browser and then you will have this:
![pending](https://user-images.githubusercontent.com/125628193/222057402-12a858ef-1722-49c2-9321-92301a7ce30e.png)
  Here we can see two things:
  * The square now is orange, this is because the program doesn't have save information of that image yet.
  * Now there is something in the image editor.

## Starting using the editor
The next step will be to use the image editor to save information of the last selected item on the square that we're using, to use the image editor we have to select a zone in the image:
![editor1](https://user-images.githubusercontent.com/125628193/222059999-b41e4e44-ab03-4e07-8430-38a3ec1fe5d4.png)

And after selecting a zone you can start to interact with the buttons below. The three bottons are respectively:
* CUT button: this will cut the zone that we selected:
![editor2](https://user-images.githubusercontent.com/125628193/222061811-9783ec04-8318-4921-8c8b-4b20b5302b7c.png)
  - When we cut the image the UI give us information in the upper right corner about the last cut that we made, we have; first the avarage of the intensity of color in the red channel for the zone that we selected and second the standard deviation that we suffer in the same.
  - When we do a cut the image in the editor will be updated to the segment that we cropped.
* RESTABILSH button: The restablish button will restore the image in the editor to the original last .tif image that we choose, this is for possible errors when cropping.
* ACCEPT button: This button will save the information of the segment of the image that we cropped, will set the color of the square to grey and will turn on the text box that is connected to the 'get image' button that we used, giving us a green background color for that text box as a signal that we already haven't a value in the box.
![text box](https://user-images.githubusercontent.com/125628193/222066054-a43991bb-1d4f-410b-ad27-86502f824129.png)

## Text box
The text box is for introducing in the program the dose that we use to irradiate the PTR that is conected to the box, to enter the dose in the text box you only need to select it like any text box, type the dose in centi Grays and press enter.
![textvo2](https://user-images.githubusercontent.com/125628193/222071461-bc1cc71f-b89e-4395-8a63-baeb304893c6.png)

After we enter a dose, we can see that the text box is now in white, that means that the program stored a dose for the linked PTR info. 
We can also see that there is a new parameter in the information on the upper right corner. The new parameter is the information about the last dose that we have introduced in the program (at first to let us know if we for example forgot to press the enter key in the box).

We can also say that we only can enter integer numbers like dose's, that's the reason because we are advertised to text the dose in cGy, but it shoudn't be a problem, taking in count that we usually use doses in the order of cGy for RT. And even if we introduce something that is not an integer, the text box will give us a message to please enter an integer.

## Repeat this section for all your EBT3 films!!!
We only need to repeat those steps with all the images and that's all for the information upload! Also, can be neccesary to say that we need to put the non irradiated EBT3 film on the get image square that have a text box of '0 cGy'

----

# 3: Getting the calibration curve
After we get all the information relative to the EBT3 films (intensity of color in the red channel and the dose of the films). We can get the calibration curve! 
To get the calibration curve we only need to press one of these two buttons:
![GetCurve](https://user-images.githubusercontent.com/125628193/222103319-2b0a90d2-6b2a-420f-9a58-8d980432add1.png)

To do a regression of 3rd or 4th order, depending the way you take your measurements. After getting your curve.
You can save the information of that curve for the future when you need it, this by clicking in the button marked as save. When we press the save button, we will open a file browser to decide where we want to save the information of our curve, giving us a .txt file like the next one:
![archivotxt](https://user-images.githubusercontent.com/125628193/222104711-e7a81ca2-33f8-47f7-8cab-0464b787eeba.png)

- The first two rows are for the #4 options called in the Main UI segment of this text. 
- The third row is the equation of our curve
- Next we have a table with the next format:
  Film|Dose|Intensity of color in the red channel|Standard deviation (of the intensity of color)|Optic Density
  ---|---|---|---|---
  This is to the medical physist know what are the values that the program is using.
- And finally we have the date that the .txt file was created.

Also the **SAVE** button will save a .png image with the plot of the curve that we saved.

----

# 4: The option get dose
When we click to the option 'OBTENER DOSIS', that stands for 'get dose', we will get this window:
![getdose](https://user-images.githubusercontent.com/125628193/222111442-6f6f3db2-a0b0-4655-ba62-6e94182bdd3e.png)

Here we have 4 zones:
5- Film to analize.
6- Image editor.
7- Calibration curve to use.
8- Get dose zone.

Here we can say that the 5 and 6 are basically the same as in the main window 1 and 2 to get the curve, we only charge an image (with the 5) and select a segment of the film image that will give us the information (with the 6), but in this case we are gonna use that information to get the point of dose where that information belongs in our pre-built calibration curve.

# 7: Calling the calibration curve
The button marked with a seven, will open the file browser, and we are supposed to choose the .txt file with the information of the calibration curve belonging to the batch of films of the film that we are analazing that we previously saved in previous steps. 
This step will charge the plot corresponding to that curve of calibration in the big white rectangle. And also will give us the equation of the curve that we selected.
![curveuploaded](https://user-images.githubusercontent.com/125628193/222113930-386f5973-1d86-48b3-8ade-0fe5a5df4823.png)

# 8: Getting the dose
After we uploeaded bot, the calibration curve information and the information of the film that we want to analize, we can finally get the desired dose!
![final](https://user-images.githubusercontent.com/125628193/222115961-7af2de3f-a67a-4f61-a7f7-1d706dfd7b04.png)

To achieve this we only need to press in the get dose button. And we will get the dose next to the get dose button and ploted in the curve.
Also we can press the sreenshot buton to open the files browser and save a screenshot of what we have.
