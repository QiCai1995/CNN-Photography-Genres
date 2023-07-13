# Classifying Photography Genres Using Convolutional Neural Networks


## Project Overview

I am solving the problem of classifying photography into landscape and portrait genres for art galleries and online stock photography platforms. I utilized an image dataset sourced from Kaggle and Unsplash to train my model. My model achieves an impressive accuracy of 99% in correctly predicting whether a photograph belongs to the landscape or portrait categories. This high accuracy demonstrates the effectiveness of my model in improving curation efficiency and enhancing the user experience on stock photography platforms.

<img src="https://imgur.com/0O23VOV.png" width = 60% height = 60%>

## Goals

The business goal for classifying photography genres into landscape and portrait categories is to increase curation efficiency and productivity, as well as enhance the user experience on art galleries and online stock photography platforms. By accurately classifying photos, these platforms can streamline the process of organizing and categorizing their vast collections of images. This allows for easier search and discovery of specific genres, making it more convenient for users to find the type of photography they are interested in. Additionally, improved curation efficiency helps ensure that the platforms present high-quality and relevant content to their users, leading to enhanced user satisfaction and engagement. Ultimately, the goal is to attract more users, increase sales or engagement on the platforms, and establish a reputation for providing curated and visually appealing content.

## Data

Data is collected from [Kaggle](https://www.kaggle.com/datasets/arnaud58/landscape-pictures) and [Unsplash](https://unsplash.com/s/photos/portrait), a total of 10,060 images in the genres of landscape and portrait. The images have various dimensions and resolutions. 

Data stored in my [Google Drive](https://drive.google.com/drive/folders/1OtEbHvzK9ffJZBXB_N7YlfEfumWvQTPA?usp=drive_link)

## Methods

#### Data Preparation:

1. Combining images from 2 folders to create the entire dataset using OpenCV. Shuffle or randomize.
   
2. Indexing classes to 0 and 1. 0 being a landscape photograph. 1 being a portrait photograph.
   
3. Separating features and targets, and creating 2 pickle files.

4. Resizing all images to 224 pixels x 224 pixels.
   
5. Converting color images to greyscale.

6. Apply Augmentation to increase the diversity of the training data including image rotation, horizontal and vertical shift, shear transformation, zoom in and out on images, and horizontal and vertical flips.


#### Data Modeling:

Dummy Classifier/ baseline model: A dummy classifier has a 52% accuracy meaning correctly predicting if a landscape or portrait photograph is classified correctly at a 52% rate.

Model 1: A convolutional neural net with 2 convolutional layers and 1 dense/hidden layer, without augmentation.
Model 1A: A convolutional neural net with 2 convolutional layers and 1 dense/hidden layer, with augmentation.

Model 2: A convolutional neural net with 3 convolutional layers and 0 dense layers, with augmentation.

Model 3: A convolutional neural net with 3 convolutional layers and 0 dense layers, with augmentation, with L2 Ridge Regularization.



## Evaluation

The final model I decided to go with was Model 2 with 3 convolutional layers, 0 dense layers, with augmentation, without regularization. The accuracy is 99%, and the loss is 0.036. Compared to the baseline dummy model, model accuracy has improved by 47%.



Final Model Summary

<img src ="https://github.com/QiCai1995/CNN-Photography-Genres/blob/main/images/Final%20Model%20Summary.png" width = 60% height = 60% >





Final Model Confusion Matrix on Testing Data

<img src="https://github.com/QiCai1995/CNN-Photography-Genres/blob/main/images/Testing%20Confusion%20Matrix.png" width=50% height=50%> 





Classification Report on Testing Data

<img src="https://github.com/QiCai1995/CNN-Photography-Genres/blob/main/images/Final%20Classification%20Report.png" width=50% height=50%>



## Conlusion

Recommendation of Usage:

Automatic Genre Classification: create an automated system that automatically assigns genre labels (landscape or portrait) to incoming photographs. This can significantly reduce manual effort and increase efficiency in the curation process for art galleries and online stock photography platforms.

Content Filtering and Search: Integrate the model into the platform's search and filtering functionalities. Users can easily filter and search for specific genres, such as landscape or portrait, to find the type of photography they are looking for. This enhances user experience and improves the chances of users finding relevant content quickly.


## Next Steps

Model Deployment, develop good UX/UI elements for a photography genre classifier on a web app for an art gallery/museum or stock photography platform.

Continuously evaluate and monitor the model's performance to ensure it maintains high accuracy over time. 

Fine-tuning or retraining the model periodically with new data may also be necessary to adapt to evolving trends and changes in user preferences.

Expand genres into human portrait, animal portrait, natural landscape, and urban landscape for more specific categories.




### Links

[Final Notebook](https://github.com/QiCai1995/CNN-Photography-Genres/blob/main/Final_Notebook.ipynb)

[Presentation](https://github.com/QiCai1995/CNN-Photography-Genres/blob/main/Presentation.pdf)


