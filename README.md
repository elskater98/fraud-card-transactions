# Credit Card Transactions Fraud Detection

Over the years, the usage of credit cards has increased considerably, as it makes it easier for the user to perform
purchases without having to go to an ATM, just over the Internet. This is a direct consequence of what the world is
actually experiencing, a global digitalization process on all senses.

In every area of life, there are currently lots of technologies involved, even when talking about money transactions as
the currencies are becoming digital as well. But with the beginning of COVID-19, everything has been accelerated, causing at
the same time a rise in cybercrime and insecurity among users. For this reason, creating a product that can detect,
predict and prevent fraudulent transactions would make things easier for those companies aiming to offer
security and confidence to their users.

This repository aims to define, based on the previous premises, the basis for the design and development the project,
setting the starting point for building a comprehensive model to fill such requirements.

## About the Dataset

This is a simulated credit card transaction [dataset](https://www.kaggle.com/kartik2112/fraud-detection) containing
legitimate and fraud transactions from the duration 1st Jan 2019 - 31st Dec 2020. It covers credit cards of 1000
customers doing transactions with a pool of 800 merchants.

## Project Structure

    ├── LICENSE            <- MIT License.
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── data
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering), and
    │                         a short `-` delimited description, e.g `1.0-initial-data-exploration`.
    │
    ├── environment.yml    <- The configuration file for reproducing the environment using `conda`.
    │
    └── docker-compose.yml <- To run docker-compose for the creation of the spark environment.

## Environment

We use [Conda](https://docs.conda.io/en/latest/) to manage the python dependencies.
### Conda Environment
#### Create Environment

        conda create --file environment.yml

#### Activate Environment

        conda activate fraud-card-transactions

### Docker Compose (Spark)
        docker-compose up -d

## Work Flow

### Step 1: Data Exploration
In this part, we explore our dataset to identify all the relevant information, such as outliers, variables, types of values, possible problems, etc. Also, we perform an in-depth exploration of every variable in order to know whether it has a high impact in our model and if at the same time it helps us to define the best possible algorithm that we could apply.

### Step 2: Data Cleaning
From the analysis point, having set the main objectives about how to treat the data and the way to encourage the work, this part aims to parse those data values, enabling more complex computations. For instance, we drop the redundant and irrelevant variables, calculate certain additional values and rename the columns in order to make it easier the interpret the meaning of each variable.

### Step 3: Solution
Finally, in this part we decided to solve our problem by using neural network and machine learning solutions such as the Random Forest Classifier algorithm.

#### Step 3.1: Machine Learning (Random Forest Classifier)
After analyzing the available algorithms that [pyspark-ml](https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-classifier) has, we focus on supervised algorithms because our dataset use a label to describe if a transaction is fraudulent. Therefore, we decide to use Random Forest Classifier in order to classify our data because it makes it easy to interpret categorical and continuous data, it works well on a large datasets, it is not sensitive to outliers and avoids overfiting and in the end it has a high accuracy.
Otherwise, we considered using the Naive Bayes classifier because it provides better results when working with a small training dataset with relatively small features. However, when working with a huge feature list, this kind of model may not be accurate enough. 

![ML](https://i.imgur.com/fZiX3sj.png)
#### Step 3.2: Neuronal Network (Tabular)

According to our dataset and the [FastAI](https://docs.fast.ai/) library, the best way to classify our data would be using the Tabular solution, because our data is structured in rows and columns. Otherwise, using other solutions such as computer vision or natural leagues that the library has doesn't fit our problem and goals. 

![NN](https://i.imgur.com/jZUhQ6I.png)

## Conclusions
As we can see in the results of the metrics obtained from the performance, we can see that we have a little more than 99% of accuracy, which indicates that we rarely fail to perform a prediction. At first, we suspected that there was some problem in our solution since it would be quite difficult to obtain such values. However, after reviewing the code in detail and thinking about the possible causes of such high percentage, we realized the following:

- We have a dataset in which we use 70% of the values for training and 30% for testing.
- Within this data set, we have an unbalanced target variable, where 99.42% are legit transactions.
- Proportionally, it has a very small amout of cases of fraudulent transactions.
- Most of our classifier will be based on detecting patterns of correct purchases, instead of fraudulent operations.

Therefore, if we understand all the characteristics that compose this dataset, we will understand that the accuracy value is correct. As we can observe, about 99% of the generated purchases are made legitimately, therefore we can consider that it is the common scenario and that only a few cases will actually be fraudulent. This means that our algorithm will study the purchase patterns according to a large percentage of valid purchases, thus presenting some false positives. For this reason, we fail in around 1.700 transactions that we consider legit when they are in fact fraudulent. Consequently, the accuracy value is the result of the high volume of legit transactions over the total amount of cases. 

Both algorithms present similar results, but the neural network shows slightly better results in certain cases. The machine learning algorithm has a higher error rate in the detection of fraudulent transactions (false positives). On the other hand, in the neural network, the errors are more balanced, in addition to presenting a higher accuracy rate. 

Additionally, as a possible measure to increase the hit rate and reduce false positives in the prediction of fraudulent transactions, we have proposed the reduction of the volume of valid (non-fraudulent) transactions in relation to the total amount of transactions. In this way, the training would be based on numbers that are much more representative of the proportion of fraudulent cases with respect to the total number of transactions.