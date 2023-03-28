# Clustering-method-with-K-Means-of-Mall-Visitor-Dataset
This project develops a machine learning model using the Clustering (K-Means) method to determine mall customer clusters based on annual revenue versus sales levels using Python. 

The method used  is a partitioning-based clustering algorithm, namely K-Means. The dataset was obtained from the Kaggle website at https://www.kaggle.com/datasets/prateekiet/mall-customers. The dataset contains labels for customers ID, gender, age, annual income and spending score (1 - 100). Gender data needs to be labeled encoding first so that the value is numeric. To determine the number of clusters to be used in the clustering method, the previous program used the elbow method to determine the optimal k value. Based on the elbow plot method, a value of k = 5 is obtained which is then used for clustering using the fit_predict syntax from the sklearn library which is then plotted in the form of a scatter.

<p align = "center">
<img width=400px height=auto alt="image" src="https://user-images.githubusercontent.com/78911479/228194388-bff0b2ff-85bb-4514-b2e1-4602d0a1f4d4.png">
</p>

<p align = "center">
<img width=400px height=auto alt="image" src="https://user-images.githubusercontent.com/78911479/228194761-2019cd4e-f452-45ba-9d23-cdd7fd9bece7.png">
</p>
