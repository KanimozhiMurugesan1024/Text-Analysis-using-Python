import index, analyze

# example of how to read one file
single_file_tokens, single_file_bounds = index.index_file(r'output/federalist_papers/federalist_no_1.txt')

# ----------------------------------------------------------------------------
# THESE WILL ONLY WORK AFTER YOU IMPLEMENT THE FUNCTIONS
# return all documents and tokens for all of federalist papers
all_documents, all_tokens = index.index_dir(r'output/federalist_papers')

# Analyze:
# get a dictionary of the number of times a token occurs across all directories
token_counts = analyze.tokens_freq(all_tokens)
# pick a token from this list -- you can change
my_token = 'faction'
my_token_most_freq_file = analyze.token_most_occuring_file(my_token, all_documents, all_tokens)
print(my_token, ' ', 'found most often in file ', my_token_most_freq_file)
