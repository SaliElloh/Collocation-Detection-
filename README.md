# Collocation-Detection-
Implemented Chi-square and Pointwise Mutual Information (PMI) measures for collocation identification.

For more information about me, please visit my LinkedIn:

[![LinkedIn][LinkedIn.js]][LinkedIn-url]

<!-- ABOUT THE PROJECT -->

## About the Project:

### Introduction:

This project implements methods for identifying collocations in text using two association measures: Chi-Square and Pointwise Mutual Information (PMI). The main objective is to detect and rank bigram collocations based on these measures, which can be useful in various Natural Language Processing (NLP) tasks such as identifying word pairs that occur together more frequently than expected.

### Project Overview:

Collocations are combinations of words that frequently appear together in text and have a special meaning when used together. For this project, we will be calculating and comparing collocations using Chi-Square and PMI measures to identify significant bigrams in a given corpus.


### Chi-Square and PMI Measures:
* **Chi-Square**: A statistical measure used to evaluate the independence of two events (in this case, word pairs). A higher chi-square value indicates a stronger association between the words.
* **PMI**: Measures the association between two words by comparing their co-occurrence probability with the product of their individual probabilities. A higher PMI score indicates that the words occur together more often than expected.


<!-- Dataset -->

##  Dataset:

The dataset used in this project is a text file named Collocations that contains the corpus data. The text is tokenized, and both unigrams and bigrams are extracted for analysis.


### Data Example:


## Files:

The repository includes the following files:

1. **Collocation.py**: Python script containing the implementation for collocation detection using Chi-Square and PMI.
2. **Collocations**: The corpus text file for analysis.
3. **Collocations.answers**: Text file with detailed results and explanations.
4. **unigrams_bigrams.csv**: CSV file with unigrams and bigrams.
5. **unigram_bigram_counts.csv**: CSV file with unigram and bigram counts.
6. **co_occurrence_table.csv**: CSV file with the co-occurrence table.

<!-- METHODOLOGY -->

## Methodology

### Algorithm Steps:

  1. **Data Loading**
      - **Read Corpus**:
        - Open the "collocations" file and read its contents into a list of words.
  
  2. **Data Cleaning and Preparation**
       - **Filter Out Punctuation**:
         - Use a regular expression to filter out words that do not match the word pattern, retaining only valid word
  
  3. **Feature Extraction**
      - **Create Unigrams and Bigrams**:
        - Extract unigrams (individual words) and bigrams (pairs of consecutive words) from the cleaned data.
      - **Save to CSV**:
        - Save the unigrams and bigrams to "unigrams_bigrams.csv" for reference.

  4. **Count Calculation**
      - **Count Unigrams and Bigrams**:
        - Initialize dictionaries to store counts for unigrams and bigrams.
        - Calculate the frequency of each unigram and bigram.
      - **Save Counts to CSV**:
        - Save the unigram and bigram counts to "unigram_bigram_counts.csv".

  5. **Statistical Analysis**
      - **Calculate Total Observations**:
        - Determine the total number of words in the corpus (N).
      - **Generate Occurrence Table**:
        - Define a function to calculate the 2x2 occurrence table matrix for each bigram in the corpus.
      - **Perform Statistical Tests**:
        - Define functions to calculate normalized Chi-Square, Chi-Square, and PMI scores for bigrams.

  6. **Score Calculation and Evaluation**
      - **Analyze Bigrams**:
        - Compute normalized Chi-Square, Chi-Square, and PMI scores for each bigram and store these scores in dictionaries.
      - **Sort and Output Top Bigrams**:
        - Sort the bigrams based on normalized Chi-Square, Chi-Square, and PMI scores
        - Print the top 20 bigrams for each measure.


### Example:
   
<!-- Results -->
## How to Run the Project

1. **Clone the Repository**:

    
2. **run the Script**:
 

3. **View Results**:


<!-- Results -->

## Results:


<!-- Built With -->

## Built With:

The frameworks and libraries used within this project are:

* [![Python][Python.js]][Python-url]
* [![NumPy][NumPy.js]][NumPy-url]
* [![Datetime][Datetime.js]][Datetime-url]


<!-- CONTACT -->

## Contact

Sali E-loh - [@Sali El-loh](https://www.linkedin.com/in/salielloh12/) - ellohsali@gmail.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[LinkedIn.js]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[LinkedIn-url]: https://www.linkedin.com/in/salielloh12/

[Python.js]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[NumPy.js]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[Datetime.js]: https://img.shields.io/badge/Datetime-44a833?style=for-the-badge
[Datetime-url]: https://docs.python.org/3/library/datetime.html



