import sys
import csv
import json

# A python script to convert a csv file into a json file suitable for d3.
# DS thought this might come in handy if we decide to make the visualizations in d3.

# Set debug mode to true for verbose output.
debug_mode = True
if debug_mode: print("[START] Start the csv to json conversion script in debug mode!")

# Converter function
def csv_to_json(path_to_csv, name_of_csv, path_to_json, name_of_json):
    try:
        if debug_mode: print("    Start csv to json function...")
        data = {"observations": []} # The data is ultimately a list of observations.
        # Read the csv file assuming utf-8 encoding.
        if debug_mode: print("    Read csv file from " + path_to_csv + name_of_csv + "...")
        with open (path_to_csv + "\\" + name_of_csv, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            on_header = True
            header = ()
            if debug_mode: print("    Loop through each row of the csv...")
            for row in csv_reader:
                data['observations'].append(row)
        if debug_mode: print("    End file iteration and close loop...")
        # Write the object to the file system as json with utf-8 encoding.
        if debug_mode: print("    Write data to the file system as json...")
        with open(path_to_json + "\\" + name_of_json, 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(data, allow_nan = False, indent = 4))
        if debug_mode: print("    End csv to json function...")
    except csv.Error as error:
        print("[ERROR] THE IMPORTED CSV LIBRARY HAS THROWN AN EXCEPTION:")
        raise
    except json.JSONDecodeError as error:
        print("[ERROR] THE IMPORTED JSON LIBRARY HAS THROWN AN EXCEPTION:")
        raise
    except Exception as error:
        print("[ERROR] AN UNCAUGHT EXCEPTION WAS DETECTED IN THE CSV_TO_JSON METHOD:")
        raise

# Script driver.
try:
    if len(sys.argv) > 0:
        if sys.argv[1] == '-b': # convert a batch of csv files.
            if debug_mode: print("    Run the script for several files...")
            path_to_csv = sys.argv[2]
            path_to_json = sys.argv[2]
            for file_name in sys.argv[3:]:
                csv_to_json(path_to_csv, file_name + ".csv", path_to_json, file_name + ".json")
        elif sys.argv[1] == '-i': # convert an individual csv from the console.
            if debug_mode: print("    Run the script once with console arguments...")
            csv_to_json(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        else: raise Exception("Unrecognized console argument.")
    else: # Run with embedded script constants
        if debug_mode: print("    Run the script with constant path values...")
        path_to_csv = r''
        name_of_csv = r''
        path_to_json = r''
        name_of_json = r''
        csv_to_json(path_to_csv, name_of_csv, path_to_json, name_of_json)
except Exception as error:
    print("[ERROR] AN UNCAUGHT EXCEPTION WAS DETECTED IN THE SCRIPT DRIVER:")
    raise
if debug_mode: print("[END] End of the csv to json conversion script!")