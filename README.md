# Project Proposal
For millennia, humans have predicted climate patterns in order to properly structure their lives and activities. Whether it be for ensuring a safe journey or drawing great crop yields, forecasting the climate has been a catalyst for the development of human civilization. The same rings true today. In the face of climate change, humans have once again found the need to increase the accuracy of their climate predictions to save lives and maintain order. In this project, I have set out to predict the predefined target variables.

I will be using the following dataset from kaggle.com. Both the training and test sets are generated by E3SM-MMF climate model, a model that combines cloud physics with massive exascale throughput and published by an Arxiv lab group called ClimSim.

This will be a supervised regression problem. The independent and target variables have already been defined in the link provided above. Since this dataset has many target variables, I believe that it will require an approach resembling deep learning.

The dataset has already been split into the training and test data, with the training set accounting for more than 10 million samples, while the test set has 625000 samples. Since the training data has millions of samples and there are only 4 missing values, I will drop those samples. I intend to use the IQR method to identify any outliers and remove the samples containing them, if they are relatively infrequent. Otherwise, I anticipate that a log transformation will make outliers less impactful on any conclusions.

As part of the exploratory data analysis (EDA), I will first get the IQR of all the features, so I can identify outliers. Then, I will create a correlation matrix to see what features are related/irrelevant to each other. After that, I will use data visualizations like scatter plots, line plots, and heatmaps for additional exploration. This will allow me to create a more focused and plausible hypothesis. Depending on what relations are found between features, it may become beneficial to conduct a PCA, in order to reduce the dimensionality of the dataset (many features have 60 dimensions).

# Survey Existing Research
[Link](https://docs.google.com/document/d/1yJoqTdEhT7qudbydGBeaO0jKNYxtCi66W0P4fGvPYPg/edit?usp=sharing)
