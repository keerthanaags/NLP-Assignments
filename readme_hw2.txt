Name: Keerthanaa G Saminathan
ID  : 1750117

the python code doesn't take any command line arguments.
To run the code, use

python3 keerthanaa_hw2_viterbi.py

- The inputs from the assignment question have been initialized inside the program
- The transition probability is stored as a dataframe where df[row][column] represents the transition probability from column->row
- The emission probability is stored in a dictionary
- The viterbi matrix is computed by iterating through each column (word)
- The final solution is computed by backtracking through the viterbi path matrix

- The program prints the inputs, the viterbi matrix and the final solution of the tagger
