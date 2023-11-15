# PL_election_results_analyzer
App that analyze the election results 

This Python application is designed for analyzing election results across different electoral districts using CSV file data. It provides insights into voter turnout for different institutions (like Sejm and Senate in the Polish context) and visualizes the data through a bar chart.

Features
CSV File Analysis: Reads election data from CSV files, distinguishing between different institutions (e.g., Sejm and Senate).
Voter Turnout Comparison: Calculates the difference in the number of voters for each institution.
Data Storage: Saves the analyzed data into a new CSV file with a unique identifier.
Graphical Representation: Creates a bar chart to visually compare voter turnout, highlighting the difference.

Installation
Python Environment: Ensure you have Python installed on your system.
Required Libraries: The application requires csv for file handling and matplotlib for chart generation. Install these libraries using pip if not already installed.
Usage
Run the Application: Launch the script in a Python environment.
File Inputs: Input the names of the CSV files when prompted. The first file should contain election data, and the second file name is for saving results.
View Results: The application will display a bar chart showing the number of voters for each institution and the difference in their turnouts.

Code Components
Class Analizator_Wynikow_Wyborow: The main class handling all functionalities.
__init__: Initializes the class with file names.
licz_roznice: Reads the CSV file, calculates differences in voter turnout.
zapisz_do_pliku: Writes analyzed data into a new CSV file.
rysuj_wykres: Generates a bar chart visualizing the data.

Running the Application
Execute the script in a Python environment. You'll be prompted to enter the names of two CSV files. The first file should contain the election data, and the second one is for output.

Support
For issues, suggestions, or contributions, feel free to open an issue or a pull request on the repository where this application is hosted.
Note: The code and its functionality are designed around the structure of a specific CSV file format. Adjustments may be needed for different data structures or election systems.





