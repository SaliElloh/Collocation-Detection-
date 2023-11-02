import re
import math
import csv

import datetime

time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(time)


# Open the file for reading
with open("collocations", "r") as file:
    word_list = []

    for line in file:
        words = line.strip().split()
        word_list.extend(words)

word_pattern = re.compile(r'\w+')

# Use list comprehension to filter out punctuation
word_list = [word for word in word_list if word_pattern.match(word)]

unigrams = word_list
bigrams = [(word_list[i], word_list[i + 1]) for i in range(len(word_list) - 1)]

csv_file = "unigrams_bigrams.csv"

# Combine unigrams and bigrams into pairs
data = list(zip(unigrams, bigrams))

#create Unigrams and bigrams csv file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Unigrams", "Bigrams"])
    for row in data:
        writer.writerow([row[0], f"{row[1][0]} {row[1][1]}"])
# counting the unigram and bigram

unigram_counts = {}
bigram_counts = {}

for unigram in unigrams:
    if unigram not in unigram_counts:
        unigram_counts[unigram] = 0
    unigram_counts[unigram] += 1

for bigram in bigrams:
    if bigram not in bigram_counts:
        bigram_counts[bigram] = 0
    bigram_counts[bigram] += 1


#store the count in an csv file
csv_file = "unigram_bigram_counts.csv"

data = []

for unigram, count in unigram_counts.items():
    data.append([unigram, count, "", ""])  # Adding an empty string for bigram columns
for bigram, count in bigram_counts.items():
    data.append(["", "", " ".join(bigram), count])

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Unigrams", "Unigram Counts", "Bigrams", "Bigram Counts"])
    writer.writerows(data)

# N , total number of observances:
N = len(word_list)


#function to calculate the occurrence table matrix used for PMI and chi-square
def calculate_occurrence_table(bigram, corpus):
    """
    Calculate the 2x2 occurrence table matrix for a given bigram in a corpus.
    """
    first_word, second_word = bigram
    N = len(corpus)

    # Count occurrences of both words in the bigram
    both_count = bigram_counts.get(bigram, None)

    # Count occurrences of the second word without the first word
    second_count = 0
    for i in range(len(corpus) - 1):
        if corpus[i] == second_word and corpus[i + 1] != first_word:
            second_count += 1

    # Count occurrences of the first word without the second word
    first_count = 0
    for i in range(1, len(corpus)):
        if corpus[i - 1] == first_word and corpus[i] != second_word:
            first_count += 1

    # Calculate the count of neither of the words
    neither_count = N - (second_count + first_count)

    # 2x2 occurrence table matrix
    occurrence_table = [[both_count, second_count], [first_count, neither_count]]

    return occurrence_table

#create two chi-square test, normalized and not normalized
def normalized_chi_square_test(occurrence_table):
    """
    Perform a chi-square test on a 2x2 occurrence table.
    """
    # Extract values from the occurrence table
    a, b = occurrence_table[0]
    c, d = occurrence_table[1]

    # Calculate expected values for each cell
    total = a + b + c + d

    expected_a = ((a + c)/N) * ((a + b)/N)*N
    expected_b = ((a + c)/N)* ((b + d)/N)*N
    expected_c = ((c + d)/N) * ((a + b)/N)*N
    expected_d = ((c + d)/N) * ((b + d)/N)*N

    chi_square = ((a - expected_a) ** 2 / expected_a) + ((b - expected_b) ** 2 / expected_b) + \
                 ((c - expected_c) ** 2 / expected_c) + ((d - expected_d) ** 2 / expected_d)

    return chi_square



def calculate_pmi(occurrence_table):
    """
    Calculate the Pointwise Mutual Information (PMI) score for a given occurrence table.
    """
    a, b, c, d = occurrence_table[0][0], occurrence_table[0][1], occurrence_table[1][0], occurrence_table[1][1]
    # Calculate probabilities
    P_a_b = a / (a + b + c + d)
    P_a = (a + c) / (a + b + c + d)
    P_b = (a + b) / (a + b + c + d)
    # Calculate PMI
    pmi = math.log2(P_a_b / (P_a * P_b))

    return pmi

corpus = word_list

print(len(corpus))

# Calculate normalized and regular chi-square scores for all bigrams and store them in a dictionary
normalized_chi_square_scores = {}

#calculate pmi_scores
pmi_scores = {}

for bigram in bigram_counts:
    matrix = calculate_occurrence_table(bigram, corpus)
    #normalized Chi square (multiplied by N)
    normalized_chi_square = normalized_chi_square_test(matrix)
    normalized_chi_square_scores[bigram] = normalized_chi_square

    pmi = calculate_pmi(matrix)
    pmi_scores[bigram] = pmi
# Sort the bigrams by their normalized chi-psquare scores in reverse order
normalized_sorted_chi = sorted(normalized_chi_square_scores.items(), key=lambda x: x[1], reverse=True)


# Output the top 20 normal chi bigrams
normalized_top_20_chi = normalized_sorted_chi[:20]
for bigram, chi in normalized_top_20_chi:
    print(f"Bigram: {bigram} Normalized Chi Score: {chi}")


# Sort the bigrams by PMI score in descending order
sorted_pmi = sorted(pmi_scores.items(), key=lambda x: x[1], reverse=True)

# Print the top 20 bigrams
top_20_pmi = sorted_pmi[:20]
for bigram, pmi in top_20_pmi:
    print(f"Bigram: {bigram} PMI Score: {pmi}")





