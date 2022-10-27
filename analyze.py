
def tokens_freq(all_tokens):
    token_f = {}
    for onetoken in all_tokens:
        a = all_tokens[onetoken]
        token_f[onetoken] = len(a)
    return token_f

    """Returns a count of how many times a token occurs across all documents.

    Args:
        all_tokens (dict): tokens output from index.index_dir

    Returns:
        token_frequency (dict): A dictionary of {token: count}, where count
            is the count of all the occurences of token in a directory of files.
        """


def token_most_occuring_file(token_name, all_documents, all_tokens):
    if not token_name in all_tokens:
        return "Token not present"
    a = all_tokens[token_name]
    occurance_freq = {}
    m_occurance_doc = []
    m_occurance = 0
    for occurance in a:
        if occurance[0] in occurance_freq:
            occurance_freq[occurance[0]] = occurance_freq[occurance[0]] + 1
        else:
            occurance_freq[occurance[0]] = 1
        if m_occurance < occurance_freq[occurance[0]]:
             m_occurance = occurance_freq[occurance[0]]
             m_occurance_doc = []
             m_occurance_doc.append(all_documents[occurance[0]] ['path'])
        elif m_occurance == occurance_freq[occurance[0]]:
            m_occurance_doc.append(all_documents[occurance[0]] ['path'])
    return m_occurance_doc



    """Returns the path to the file that has the most occurances of token_name.

    Args:
        token_name (string): the token to lookup
        all_documents (dictionary): documents output from index.index_dir
        all_tokens (dictionary): tokens output from index.index_dir

    Returns:
        file_path (string): The path to the file in the directory where the
            input token_name occurs the most.
    """
