import numpy as np
import pandas as pd

# Input sentence
print("The input sentence for tagging is: \"learning changes everything\"")
sentence = "start learning changes throughly end"
column_header = sentence.split(' ')
column_size = len(column_header)
print("Sentence tokens:",column_header)

# Load POS types
types = "start noun verb adverb end"
row_header = types.split(' ')
print("\nThe parts of the speech types are:",row_header)
row_size = len(row_header)

# Load transition probabilities as a dataframe
transitions = np.reshape((0.0,0.0,0.0,0.0,0.0,0.2,0.1,0.4,0.0,0.0,0.3,0.3,0.1,0.0,0.0,0.0,0.1,0.4,0.0,0.0,0.0,0.0,0.0,0.1,0.0), (row_size,row_size))
transition_prob = pd.DataFrame(transitions, columns=row_header, index=row_header)

print("\nTransition probability:")
print(transition_prob)

# Load emission probabilities into a dictionary
emission_prob = {'learning|verb':0.003, 'changes|verb':0.004, 'throughly|adverb':0.002, 'learning|noun':0.001, 'changes|noun':0.003, 'end|end':1.0}
print("\nEmission probability:")
print(emission_prob)

# Initialize a dataframe for viterbi matrix with the row*column size
viterbi_matrix = np.reshape((0.0,)*(column_size*row_size), (row_size,column_size))
viterbi_df = pd.DataFrame(viterbi_matrix, columns=column_header, index=row_header)

# This dataframe is to keep track of the path inorder to do backtracking after computing all the matrix values
viterbi_path = pd.DataFrame(np.reshape(('none',)*(column_size*row_size), (row_size,column_size)),columns=column_header, index=row_header)

# Start the loop for calculating the probabilities
print("\nComputing Viterbi Matrix...")
# Iterating column by column in the matrix
for i in range(column_size):
    # Initializing the start value as 1.0 as any sentence always begins with start
    if i==0:
        viterbi_df.loc['start']['start'] = 1.0
    else:
        # Considering each POS type for the current word
        for pos in row_header:
            # Calculate probabilities for all previous possibilities and find the maximum
            max_prob = 0.0
            max_pos = 'none'
            for prev_pos in row_header:
                # Get the corresponding transition and emission probabilities
                emission_key = column_header[i] + "|" + pos
                transition_value = transition_prob[prev_pos][pos]
                emission_value = 0.0
                if emission_key in emission_prob:
                    emission_value = emission_prob[emission_key]
                val = viterbi_df.loc[prev_pos][column_header[i-1]]*transition_value*emission_value
                if val > max_prob:
                    max_prob = val
                    max_pos = prev_pos
            viterbi_df.loc[pos][column_header[i]] = max_prob
            viterbi_path.loc[pos][column_header[i]] = max_pos

print("\nThe Viterbi Matrix is:")
print(viterbi_df)


# Determining and printing the solution using viterbi_path dataframe
print("\nBacktracking to find the solution...")
solution = []
solution.append('end')

val = viterbi_path.loc['end']['end']
column_index = column_size-2
while val!='none':
    solution.append(val)
    val = viterbi_path.loc[val][column_header[column_index]]
    column_index-=1

print("\nThe solution is:")
for word in column_header:
    print(word,'-',solution.pop())
