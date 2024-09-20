punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word  

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(text):
    # Convert the input text to lowercase and split it into words
    words = text.lower().split()
    
    # Initialize a counter for positive words
    positive_word_count = 0
    
    for word in words:
        # Strip punctuation from the word
        word = strip_punctuation(word)
        
        # Check if the word is in the positive_words list
        if word in positive_words:
            positive_word_count += 1

    return positive_word_count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(text):
    # Convert the input text to lowercase and split it into words
    words = text.lower().split()
    
    # Initialize a counter for negative words
    negative_word_count = 0
    
    for word in words:
        # Strip punctuation from the word
        word = strip_punctuation(word)
        
        # Check if the word is in the negative_words list
        if word in negative_words:
            negative_word_count += 1

    return negative_word_count

           
# Define the functions for strip_punctuation, get_pos, and get_neg as shown previously

# Open the project_twitter_data.csv file for reading
with open("project_twitter_data.csv", "r") as twitter_data:
    # Read the first line (header) and ignore it
    twitter_data.readline()

    # Open a text file (resulting_data.txt) for writing
    with open("resulting_data.csv", "w") as resulting_data:
        # Write the header to the resulting_data file
        resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    
        # Process each line in the input file
        for line in twitter_data:
            # Split the line into fields
            fields = line.strip().split(",")
            
            # Extract the fields
            tweet, retweets, replies = fields[0], int(fields[1]), int(fields[2])
    
            # Calculate the positive and negative scores
            positive_score = get_pos(tweet)
            negative_score = get_neg(tweet)
    
            # Calculate the net score
            net_score = positive_score - negative_score
    
            # Write the results to the text file
            resulting_data.write(f"{retweets}, {replies}, {positive_score}, {negative_score}, {net_score}\n")

print("Data written to resulting_data.csv")
