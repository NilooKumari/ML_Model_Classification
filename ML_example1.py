# Niloo Kumari
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Machine Learning on the iris dataset\n",
    "    - Supervised learning model\n",
    "    - Predict the species of an iris using the measurements (sepal length, sepal width, petal length, petal width)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Loading the iris dataset into scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import load_iris function from datasets module\n",
    "from sklearn.datasets import load_iris"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "sklearn.utils.Bunch"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Save \"bunch\" object containing iris dataset and its attributes\n",
    "iris=load_iris()\n",
    "type(iris)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5.1 3.5 1.4 0.2]\n",
      " [4.9 3.  1.4 0.2]\n",
      " [4.7 3.2 1.3 0.2]\n",
      " [4.6 3.1 1.5 0.2]\n",
      " [5.  3.6 1.4 0.2]\n",
      " [5.4 3.9 1.7 0.4]\n",
      " [4.6 3.4 1.4 0.3]\n",
      " [5.  3.4 1.5 0.2]\n",
      " [4.4 2.9 1.4 0.2]\n",
      " [4.9 3.1 1.5 0.1]\n",
      " [5.4 3.7 1.5 0.2]\n",
      " [4.8 3.4 1.6 0.2]\n",
      " [4.8 3.  1.4 0.1]\n",
      " [4.3 3.  1.1 0.1]\n",
      " [5.8 4.  1.2 0.2]\n",
      " [5.7 4.4 1.5 0.4]\n",
      " [5.4 3.9 1.3 0.4]\n",
      " [5.1 3.5 1.4 0.3]\n",
      " [5.7 3.8 1.7 0.3]\n",
      " [5.1 3.8 1.5 0.3]\n",
      " [5.4 3.4 1.7 0.2]\n",
      " [5.1 3.7 1.5 0.4]\n",
      " [4.6 3.6 1.  0.2]\n",
      " [5.1 3.3 1.7 0.5]\n",
      " [4.8 3.4 1.9 0.2]\n",
      " [5.  3.  1.6 0.2]\n",
      " [5.  3.4 1.6 0.4]\n",
      " [5.2 3.5 1.5 0.2]\n",
      " [5.2 3.4 1.4 0.2]\n",
      " [4.7 3.2 1.6 0.2]\n",
      " [4.8 3.1 1.6 0.2]\n",
      " [5.4 3.4 1.5 0.4]\n",
      " [5.2 4.1 1.5 0.1]\n",
      " [5.5 4.2 1.4 0.2]\n",
      " [4.9 3.1 1.5 0.1]\n",
      " [5.  3.2 1.2 0.2]\n",
      " [5.5 3.5 1.3 0.2]\n",
      " [4.9 3.1 1.5 0.1]\n",
      " [4.4 3.  1.3 0.2]\n",
      " [5.1 3.4 1.5 0.2]\n",
      " [5.  3.5 1.3 0.3]\n",
      " [4.5 2.3 1.3 0.3]\n",
      " [4.4 3.2 1.3 0.2]\n",
      " [5.  3.5 1.6 0.6]\n",
      " [5.1 3.8 1.9 0.4]\n",
      " [4.8 3.  1.4 0.3]\n",
      " [5.1 3.8 1.6 0.2]\n",
      " [4.6 3.2 1.4 0.2]\n",
      " [5.3 3.7 1.5 0.2]\n",
      " [5.  3.3 1.4 0.2]\n",
      " [7.  3.2 4.7 1.4]\n",
      " [6.4 3.2 4.5 1.5]\n",
      " [6.9 3.1 4.9 1.5]\n",
      " [5.5 2.3 4.  1.3]\n",
      " [6.5 2.8 4.6 1.5]\n",
      " [5.7 2.8 4.5 1.3]\n",
      " [6.3 3.3 4.7 1.6]\n",
      " [4.9 2.4 3.3 1. ]\n",
      " [6.6 2.9 4.6 1.3]\n",
      " [5.2 2.7 3.9 1.4]\n",
      " [5.  2.  3.5 1. ]\n",
      " [5.9 3.  4.2 1.5]\n",
      " [6.  2.2 4.  1. ]\n",
      " [6.1 2.9 4.7 1.4]\n",
      " [5.6 2.9 3.6 1.3]\n",
      " [6.7 3.1 4.4 1.4]\n",
      " [5.6 3.  4.5 1.5]\n",
      " [5.8 2.7 4.1 1. ]\n",
      " [6.2 2.2 4.5 1.5]\n",
      " [5.6 2.5 3.9 1.1]\n",
      " [5.9 3.2 4.8 1.8]\n",
      " [6.1 2.8 4.  1.3]\n",
      " [6.3 2.5 4.9 1.5]\n",
      " [6.1 2.8 4.7 1.2]\n",
      " [6.4 2.9 4.3 1.3]\n",
      " [6.6 3.  4.4 1.4]\n",
      " [6.8 2.8 4.8 1.4]\n",
      " [6.7 3.  5.  1.7]\n",
      " [6.  2.9 4.5 1.5]\n",
      " [5.7 2.6 3.5 1. ]\n",
      " [5.5 2.4 3.8 1.1]\n",
      " [5.5 2.4 3.7 1. ]\n",
      " [5.8 2.7 3.9 1.2]\n",
      " [6.  2.7 5.1 1.6]\n",
      " [5.4 3.  4.5 1.5]\n",
      " [6.  3.4 4.5 1.6]\n",
      " [6.7 3.1 4.7 1.5]\n",
      " [6.3 2.3 4.4 1.3]\n",
      " [5.6 3.  4.1 1.3]\n",
      " [5.5 2.5 4.  1.3]\n",
      " [5.5 2.6 4.4 1.2]\n",
      " [6.1 3.  4.6 1.4]\n",
      " [5.8 2.6 4.  1.2]\n",
      " [5.  2.3 3.3 1. ]\n",
      " [5.6 2.7 4.2 1.3]\n",
      " [5.7 3.  4.2 1.2]\n",
      " [5.7 2.9 4.2 1.3]\n",
      " [6.2 2.9 4.3 1.3]\n",
      " [5.1 2.5 3.  1.1]\n",
      " [5.7 2.8 4.1 1.3]\n",
      " [6.3 3.3 6.  2.5]\n",
      " [5.8 2.7 5.1 1.9]\n",
      " [7.1 3.  5.9 2.1]\n",
      " [6.3 2.9 5.6 1.8]\n",
      " [6.5 3.  5.8 2.2]\n",
      " [7.6 3.  6.6 2.1]\n",
      " [4.9 2.5 4.5 1.7]\n",
      " [7.3 2.9 6.3 1.8]\n",
      " [6.7 2.5 5.8 1.8]\n",
      " [7.2 3.6 6.1 2.5]\n",
      " [6.5 3.2 5.1 2. ]\n",
      " [6.4 2.7 5.3 1.9]\n",
      " [6.8 3.  5.5 2.1]\n",
      " [5.7 2.5 5.  2. ]\n",
      " [5.8 2.8 5.1 2.4]\n",
      " [6.4 3.2 5.3 2.3]\n",
      " [6.5 3.  5.5 1.8]\n",
      " [7.7 3.8 6.7 2.2]\n",
      " [7.7 2.6 6.9 2.3]\n",
      " [6.  2.2 5.  1.5]\n",
      " [6.9 3.2 5.7 2.3]\n",
      " [5.6 2.8 4.9 2. ]\n",
      " [7.7 2.8 6.7 2. ]\n",
      " [6.3 2.7 4.9 1.8]\n",
      " [6.7 3.3 5.7 2.1]\n",
      " [7.2 3.2 6.  1.8]\n",
      " [6.2 2.8 4.8 1.8]\n",
      " [6.1 3.  4.9 1.8]\n",
      " [6.4 2.8 5.6 2.1]\n",
      " [7.2 3.  5.8 1.6]\n",
      " [7.4 2.8 6.1 1.9]\n",
      " [7.9 3.8 6.4 2. ]\n",
      " [6.4 2.8 5.6 2.2]\n",
      " [6.3 2.8 5.1 1.5]\n",
      " [6.1 2.6 5.6 1.4]\n",
      " [7.7 3.  6.1 2.3]\n",
      " [6.3 3.4 5.6 2.4]\n",
      " [6.4 3.1 5.5 1.8]\n",
      " [6.  3.  4.8 1.8]\n",
      " [6.9 3.1 5.4 2.1]\n",
      " [6.7 3.1 5.6 2.4]\n",
      " [6.9 3.1 5.1 2.3]\n",
      " [5.8 2.7 5.1 1.9]\n",
      " [6.8 3.2 5.9 2.3]\n",
      " [6.7 3.3 5.7 2.5]\n",
      " [6.7 3.  5.2 2.3]\n",
      " [6.3 2.5 5.  1.9]\n",
      " [6.5 3.  5.2 2. ]\n",
      " [6.2 3.4 5.4 2.3]\n",
      " [5.9 3.  5.1 1.8]]\n"
     ]
    }
   ],
   "source": [
    "# Print iris data\n",
    "print (iris.data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']\n"
     ]
    }
   ],
   "source": [
    "# Print the feature names\n",
    "print(iris.feature_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
      " 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
      " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2\n",
      " 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n",
      " 2 2]\n"
     ]
    }
   ],
   "source": [
    "# Print integers representing the species of each observation\n",
    "print(iris.target)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['setosa' 'versicolor' 'virginica']\n"
     ]
    }
   ],
   "source": [
    "# Print the encoding scheme for the species: 0=setosa, 1-versicolor, 2-virginica\n",
    "print(iris.target_names)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Requirements for working with data in scikit-learn\n",
    "   - Features and response are seperate objects\n",
    "   - Features and response should be numeric\n",
    "   - Features and response should be Numpy arrays\n",
    "   - Features and response should have specific shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n",
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "# Check the type of the features and response\n",
    "print(type(iris.data))\n",
    "print(type(iris.target))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(150, 4)\n"
     ]
    }
   ],
   "source": [
    "# Check the shape of the features \n",
    "print(iris.data.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(150,)\n"
     ]
    }
   ],
   "source": [
    "# Check the shape of the response\n",
    "print(iris.target.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store feature matrix in \"X\"\n",
    "X=iris.data\n",
    "\n",
    "# Store response vector in \"y\"\n",
    "y=iris.target"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## K-nearest neighbours (KNN) classification\n",
    "   - Pick a value of K\n",
    "   - Search for K observations in the training data that are \"nearest\" to the measurements of the unknown iris\n",
    "   - Use the most popular response value from the K nearest neighbours as the predicted response value for the unknown iris"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Import the class we want to use"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: \"Instantiate\" the \"estimator\"\n",
    "   - \"Estimator\" is scikit-learn's tearm for the model\n",
    "   - \"Instantiate\" means 'make an instance of'\n",
    "   - Name of the object does not matter\n",
    "   - Can specify tuning parameters during this step\n",
    "   - All parameters not specified are set to their default"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',\n",
      "           metric_params=None, n_jobs=1, n_neighbors=1, p=2,\n",
      "           weights='uniform')\n"
     ]
    }
   ],
   "source": [
    "knn=KNeighborsClassifier(n_neighbors=1)\n",
    "print(knn)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Fit the model with data (aka \"model training\")\n",
    "   - Model is learning the relationship between X and y\n",
    "   - Occurs in-place, so don't need to assign the results to some other object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',\n",
       "           metric_params=None, n_jobs=1, n_neighbors=1, p=2,\n",
       "           weights='uniform')"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn.fit(X,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Predict the response for a new observation\n",
    "   - New observations are called \"out-of-sample\" data\n",
    "   - Uses the information it learned during the model training process\n",
    "   - Returns a NumPy array\n",
    "   - Can predict for multiple observations at once"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 1])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_new=[[3,5,4,2],[5,4,3,2]]\n",
    "knn.predict(X_new)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Using a different value of K (Model tuning)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 1])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Instantiate the model (using K=5)\n",
    "knn=KNeighborsClassifier(n_neighbors=5)\n",
    "\n",
    "# Fit the model with data \n",
    "knn.fit(X,y)\n",
    "\n",
    "# Predict the response for new observations\n",
    "knn.predict(X_new)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Using a different classification model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 0])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# import the class\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "# Instantiate the model (using default parameters)\n",
    "logreg=LogisticRegression()\n",
    "\n",
    "# Fit the model with data\n",
    "logreg.fit(X,y)\n",
    "\n",
    "# Predict the response for new observations\n",
    "logreg.predict(X_new)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Comparing ML models in scikit-learn"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Evaluation procedure 1: Train and test on the entire dataset\n",
    "   - Train the model on the entire dataset\n",
    "   - Test the model on the same dataset, and evaluate how well we did by comparing the predicted response value with the true    response value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "150"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## We will first look at the logistic model\n",
    "\n",
    "# import the class\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "# Instantiate the model (using default parameters)\n",
    "logreg=LogisticRegression()\n",
    "\n",
    "# Fit the model with data\n",
    "logreg.fit(X,y)\n",
    "\n",
    "# Predict the response for new observations\n",
    "logreg.predict(X)\n",
    "\n",
    "# Store the predicted response values\n",
    "y_pred=logreg.predict(X)\n",
    "\n",
    "# Check how many predictions  were generated \n",
    "len(y_pred)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Classification accuracy:\n",
    "   - Proportion of correct predictions\n",
    "   - Common evaluation metric for classification problems\n",
    "   - Known as training accuracy when we train and test the model on the same data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.96\n"
     ]
    }
   ],
   "source": [
    "# Compute classification accuracy for the logistic regression model\n",
    "from sklearn import metrics\n",
    "print (metrics.accuracy_score(y,y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## KNN (K=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9666666666666667\n"
     ]
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "knn=KNeighborsClassifier(n_neighbors=5)\n",
    "knn.fit(X,y)\n",
    "y_pred=knn.predict(X)\n",
    "print (metrics.accuracy_score(y,y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## KNN (K=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0\n"
     ]
    }
   ],
   "source": [
    "knn=KNeighborsClassifier(n_neighbors=1)\n",
    "knn.fit(X,y)\n",
    "y_pred=knn.predict(X)\n",
    "print (metrics.accuracy_score(y,y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Problems with training and testing on the same data \n",
    "   - Goal is to estimate likely performance of a model on out-of-sample data\n",
    "   - But,maximizing training accuracy rewards overly complex models that won't necessarily generalize \n",
    "   - Unnecessarily complex models overfit the training data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Evaluation procedure 2: Train/Test Split\n",
    "   - Split the dataset into two pieces: a training set and a testing set.\n",
    "   - Train the model on the training set \n",
    "   - Test the model on the testing set, and evaluate how well we did "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(150, 4)\n",
      "(150,)\n"
     ]
    }
   ],
   "source": [
    "# Print the shape of X and y\n",
    "print (X.shape)\n",
    "print (y.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1: split X and y into training and testing sets\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(90, 4)\n",
      "(60, 4)\n"
     ]
    }
   ],
   "source": [
    "# Print the shapes of the new X objects\n",
    "print (X_train.shape)\n",
    "print (X_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(90,)\n",
      "(60,)\n"
     ]
    }
   ],
   "source": [
    "# Print the shapes of the new y objects\n",
    "print (y_train.shape)\n",
    "print (y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,\n",
       "          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,\n",
       "          verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 2: Train the model on the training data\n",
    "logreg=LogisticRegression()\n",
    "logreg.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.95\n"
     ]
    }
   ],
   "source": [
    "# Step 3: Make predictions on the testing data\n",
    "y_pred=logreg.predict(X_test)\n",
    "\n",
    "# Compare the actual response values (y_test) with predicted response values (y_pred)\n",
    "print( metrics.accuracy_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Repeat for KNN=5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9666666666666667\n"
     ]
    }
   ],
   "source": [
    "knn=KNeighborsClassifier(n_neighbors=5)\n",
    "knn.fit(X_train,y_train)\n",
    "y_pred=knn.predict(X_test)\n",
    "print( metrics.accuracy_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Repeat for KNN=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.95\n"
     ]
    }
   ],
   "source": [
    "knn=KNeighborsClassifier(n_neighbors=1)\n",
    "knn.fit(X_train,y_train)\n",
    "y_pred=knn.predict(X_test)\n",
    "print( metrics.accuracy_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Can we locate an even better value for K?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Try K=1 through K=25 and record testing accuracy \n",
    "k_range= range(1,26)\n",
    "score=[]\n",
    "for k in k_range:\n",
    "    knn=KNeighborsClassifier(n_neighbors=k)\n",
    "    knn.fit(X_train,y_train)\n",
    "    y_pred=knn.predict(X_test)\n",
    "    score.append( metrics.accuracy_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0,0.5,'Testing Accuracy')"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "# allow plot to appear within notebook\n",
    "%matplotlib inline\n",
    "\n",
    "# Plot the relationship between K  and testing accuracy\n",
    "plt.plot(k_range,score)\n",
    "plt.xlabel('Value of K for KNN')\n",
    "plt.ylabel('Testing Accuracy')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Making predictions on out-of-sample data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1])"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Instantiate the model with best known parameter\n",
    "knn=KNeighborsClassifier(n_neighbors=11)\n",
    "knn.fit(X_train,y_train)\n",
    "\n",
    "# Make prediction for out-of-sample observation\n",
    "knn.predict([[3,5,4,2]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Downsides of train/test split?\n",
    "   - Provides a high variance estimates of out-of-sample accuracy\n",
    "   - K-fold crossvalidation overcomes this limitation\n",
    "   - But, train/test split is still useful because of its flexibility and speed\n",
    "   \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
