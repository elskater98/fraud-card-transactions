# Credit Card Transactions Fraud Detection

Over the years, the usage of credit cards has increased considerably, as it makes it easier for the user to perform
purchases without having to go to an ATM, just over the Internet. This is a direct consequence of what the world is
actually suffering, a global digitalization process on all senses.

In every area of life, there are currently lots of technologies involved, even when talking about money transactions as
the currencies are becoming digital as well. But, with the beginning of COVID-19, all has been accelerated, causing at
the same time a rise in cybercrime and insecurity among users. For his reason, creating a product that can detect,
predict and prevent fraudulent transactions, would make things easier for those companies wondering how to offer
security and confidence to their users.

This repository aims to define, based on the previous premises, the basis for the design and development the project,
setting the starting point for building a comprhensive model to fill the requirements.

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

In this part, we explore our dataset to identify all the things related to the dataset, such as outliers, variables, types of values, possible problems, etc.

### Step 2: Data Cleaning
From the analysis point, having set the main objectives about how to treat the data and the way to encourage the work, this part aims to parse those data values, enabling more complex computations.

### Step 3: Solution

#### Step 3.1: Machine Learning (Random Forest Classifier)
We have chosen to use the Random Forest algorithm in order to classify our data because it makes it easy to interpret categorical and continuous data, it works well on a large datasets, it is not sensitive to outliers and avoids overfiting and in the end it has a high accuracy.

#### Step 3.2: Neuronal Network (Tabular)

According to our dataset and [FastAI](https://docs.fast.ai/) library, the best way to classify our data would be using the Tabular solution, because our data is structured in rows and columns.


## Conclusions
As we can see in the results of the metrics performed, we can see that we have a little more than 99% of accuracity, this indicates that we rarely fail to perform a perdition. First of all, we thought that we had some problem in the solution of the problem since it is difficult to obtain this value. After reviewing the code in detail and thinking about what could cause this high percentage, we realized the following:

- We have a dataset where we use 70% of the values for training and 30% for testing.
- Within this data set, we have the unbalanced target variable, where 99.42% are legit transactions.
- We have very few cases of fraudulent transactions.
- Most of our classifier will be based on detecting patterns of correct purchases and not fraudulent purchases.

Therefore, if we understand all the characteristics that compose this dataset, we will understand that the value is correct. It is because around 99% of the generated purchases are made legitly, therefore we understand that it is common and that only a few cases will be fraudulent. This means that our algorithm will study the purchase patterns according to a large percentage of legit purchases, thus making some false positives. For this reason we miss around 1.700 transactions saying that is legit when in fact is fraud. Therefore, the accuracy is given by the high volume of hones transactions and the correct decteted.

Overall we have observed that using random forest classifier we obtain better results than using tabular, because we can see how the correlation matrix is much better in one case than in the other.

