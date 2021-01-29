  ### Task 1
  
  Dataset source: https://archive.ics.uci.edu/ml/datasets/banknote+authentication
  
  Solution: [Google Collab file](https://colab.research.google.com/drive/17u8sQA24676Z6BUfe5wOL5c6h0y04weQ?usp=sharing) 
  
  Accuracy comparison - Banknote Dataset
  
 | | SVM | Neural Networks |
  |---|---|---|
  | **Accuracy** | 0.99 | 1.0000|
  
  
  ### Task 2
  
  Solution: [Google Collab file](https://colab.research.google.com/drive/11bgUQ4HvZo0dETI4roGbX2OzwP_nf6Wd?usp=sharing)
  
  ### Task 3
  
  Solution: [Google Collab file](https://colab.research.google.com/drive/17_PpsQdO4z1NumpJFSKR9Kpa5DOTqayD?usp=sharing)
  
  | | Network Size A | Network Size B |
  |---|---|---|
  | **Accuracy** | 0.8872 | 0.8854|
  
  Network Size A:
  ```
  keras.layers.Dense(300, activation = 'relu' ),
  keras.layers.Dense(100, activation = 'relu' ),
  keras.layers.Dense(100, activation = 'relu' ),
  keras.layers.Dense(100, activation = 'relu' ),
  keras.layers.Dense(10, activation = 'softmax' )])
  ```
  Network Size B:
  ```
  keras.layers.Dense(200, activation = 'relu' ),
  keras.layers.Dense(100, activation = 'relu' ),
  keras.layers.Dense(100, activation = 'relu' ),
  keras.layers.Dense(10, activation = 'softmax' )])
  ```
  
 ### Task 4
 
 Solution: [Google Collab file](https://colab.research.google.com/drive/1DuwrUPhx0PS2IRLHmlgNLDgigYBC5STo?usp=sharing)
 
 Dataset: 
Books dataset available [here](https://docs.google.com/spreadsheets/d/1JM0fo4tQZm__rK0rHjpxADmENIl5FuuztK8FMQQZd44/edit?usp=sharing) access only for users with PJATK domain
 
  | | SVM | Neural Networks |
  |---|---|---|
  | **Accuracy** | 0.75 | 0.6167 |
 
 
