# **Pokemon Identifier CNN**
This notebook is an exploratory project into creating a CNN image classifier through GPT-4 prompt engineering. There has been significant discussion into the capabilities of LLM AI models, with many arguing that AI cannot produce the high performing, intricate projects of a software engineer. While I believe this to be true, I have been hesitant to truly turn towards AI to develop smaller projects, or to create a foundation to build upon.

During my studies, I've had brief experience in developing CNNs and other neural networks. These were completed without AI assistance, and I wanted to compare how quickly I could build a similar model using AI.

The entirety of this project was completed in the span of approximately 4-5 hours. While the model performs well (99.77% accuracy) on the validation set, it does not generalize well when using unofficial artwork, such as fan art. This could be improved by utilizing a larger dataset that include fanart versions of each pokemon, but it was not thoroughly explored as it was not the purpose of this project.


## **Dataset**
This project was completed utilizing the Complete Pokemon Image Dataset from Kaggle:

https://www.kaggle.com/datasets/hlrhegemony/pokemon-image-dataset

This dataset contains a total of 2503 files representing 898 Pokemon varieties. Files were modified using *renamer.py* and *resizer.py*. Each image has been resized to 128x128.

Select images of Pokemon artwork were taken from a brief Google images search to test how well the model generalizes. If your work appears in one of these images and you would like it removed, please let me know at tyganderson@gmail.com
