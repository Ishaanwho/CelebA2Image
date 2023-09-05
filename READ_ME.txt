Hello! This is the user documentation for CelebA2Image:

--------------------------------------------------------------------------------------------------


This guide will walk you through the steps to set up and use the provided Python script and
pre-trained model to create images based on your input descriptions.
1. Step 1: Prerequisites
Before you begin, make sure you have the following prerequisites installed on your system:
Python 3.6 or higher
Required Python packages: pygame, numpy, tensorflow, matplotlib, PIL
You can install these packages using the following command:
pip install pygame numpy tensorflow matplotlib Pillow
2. Step 2: Unzip Files
Unzip the following files from the provided resources:
• GUI.py: The Python script that contains the GUI for generating images.
• generator_model.h5: The pre-trained generator model.
3. Step 3: Running the GUI
Open a terminal or command prompt.
Navigate to the directory where you saved the GUI.py and generator_model.h5 files.
Run the GUI script manually or by using the following command: python GUI.py
4. Step 4: Using the GUI
The GUI will open, displaying an input box where you can enter a description. Type a de-
scription that includes attributes like "smile," "age," "beard," "bangs," and "eyeglasses."
Press the GENERATE button to create an image based on the input description.
5. Step 5: Viewing the Generated Image
After clicking the GENERATE button, the GUI will display the generated image. The
generated image will be shown using the matplotlib window, which allows you to view
and analyze the image.

Important Notes:
• The GUI allows you to experiment with generating images based on various input
descriptions.
• The pre-trained generator model has been trained to generate images based on the
attributes provided in the input description.
• The GUI offers a convenient way to interact with the model and explore its image
generation capabilities.

Troubleshooting: If you encounter any issues or errors while running the GUI, make sure
you have all the prerequisites installed correctly. Ensure that the generator_model.h5 file is
located in the same directory as the GUI.py script.


Congratulations! You’ve successfully set up and used the GUI to generate images using the
pre-trained model. Feel free to experiment with different input descriptions to observe how
the model responds and generates images accordingly.


--------------------------------------------------------------------------------------------------




