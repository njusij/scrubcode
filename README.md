# scrubcode

##Download the Code
Make sure you have downloaded the Python scrub.py file and placed it in a directory on your computer.

##Prepare input files:
You need two input files. one containing the list of sensitive fields. You can name it sensitive_fields.txt and another containing the JSON data to be scrubbed. 
You can name it input.json or what names you prefer but make sure you make chnges in the code provided to reflect teh file names.

##Run the Script:
Open a terminal or command prompt
Navigate to the directory where you saved the Python scrub.py and your input files.
Before running ensure you replace sensitive_fields.txt with the path to your sensitive fields file, input.json with the path to your JSON data file, and output.json with the desired output file path

##Run the script by typing the following command and pressing Enter
python scrub.py sensitive_fields.txt input.json output.json

##Verify output:
After running the script, it will read the input files, scrub the sensitive information from the JSON data, and save the modified data to the specified output.json file.
You can open output.json to view the scrubbed JSON data.
