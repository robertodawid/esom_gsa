import sys
import pandas as pd
import os

def main(input_files, output_file):
    # Initialize a list to store the data
    data = []
    output_file = str(output_file) 

    # Loop over the input files
    for input_file in input_files:
        # Extract the model run from the input file path
        filename = os.path.basename(input_file)
        model_run = filename.split('.')[0]

        # Read the input file and extract the objective value and status
        with open(input_file, 'r') as f:
            lines = f.readlines()
            #objective_value = lines[0].split('=')[1].strip()
            # Extract the objective value from the second line
            objective_value_line = lines[1]
            objective_value = objective_value_line.split('=')[1].strip()
            status = 'Solved with gurobi'  
            # Append the data to the list
            data.append([model_run, objective_value, status])

    # Convert the list to a DataFrame
    df = pd.DataFrame(data, columns=['JOB', 'OBJECTIVE', 'STATUS'])

    # Write the DataFrame to the output file
    df.to_csv(output_file, index=False)
    

if __name__ == '__main__':

    # Get the command-line arguments
    
    input_files = snakemake.input[0:]
    output_file = snakemake.output[0]

    # Call the function
    main(input_files, output_file)