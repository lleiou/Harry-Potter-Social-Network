---
title: "When Text Mining meets Harry Potter series"
author: "Ao liu, Chenlu Ji, Hexiu Ye, Yueying Teng, Yusen Wang"  
date: "04/27/2016"
output: html_document
---

### To see our app:http://lleiou.github.io/4249FinalProject/index.html

### Contents:
#### 1. Introduction <a name="1"></a>
#### 2. Raw Text processing <a name="2"></a>
#### 3. Text Mining <a name="3"></a>
#### 4. Network Building <a name="4"></a>
#### 5. Sorting Hat <a name="5"></a>
  
## [1 Introduction](#1)
In this project, we explored the Harry Potter series using text mining techniques and visualized the network of the leading characters. Moreover, an interactivce webpage was created to mimic the job of the sorting hat in the novel.

## 2 Raw Text Processing
+  Name Entity Recognization

The complete novel was downloaded from: https://github.com/abishekk92/potter/tree/master/dataset
First,each novel was read by Python line by line to a new text file. Following this, a dictionary containing each character's fullname and nicknames called ep_nick was created for evry book. These fullnames were detected by using a package called nltk in Python and put into a list that is combined with each character's nicknames that we obtained from the Internet.

## 3 Text Mining
+  Obtain Summary Using PageRank

After removing all the stopwords, we calcualted the cosine similarity between each pair of sentences and created a matrix containing all the indexed sentences to storet the cosine similarity obtained before. This matrix was the used as the input that was fed into the Pagerank algorithm in NetworkX Python. The top ten sentences with the highest Pagerank score was used as our summarization.

+ WordCloud

We created worldcoulds for each novel. In order to make the wordcloud more meaningful, apart from removing all the stopwords, we also deleted the names of the three main characters: Harry, Ron and Hermione, in all situations.

Book1:
<p align="center"><img src="output/word cloud/book1.png" width=450 height=300></p>

Book7:
<p align="center"><img src="output/word cloud/book7.png" width=450 height=300></p>

## 4 Network Building
+  Building Network using Adaboost 

We extracted two features, polarity and subjectivity, from the processed text file using sentiment analysis. Furthermore, a co-coccurrence matrix was procuded for each novel that counts the the number of occurrence of each pair of characters. The two features were normalized using the entries in the co-occurrence matrix and these features were taken by Adaboost to classify between characters with positive realationships and those with negative relationships. 

## 5 Sorting Hat 
+  The Sorting Hat

We built a multi-class classifier that performs the job of the Sorting Hat in the novel. We parsed the following personal information: name, gender, eyecolor, hair color and House, for each character of our age who attended Hogwarts as features. Also we used random forest as classifier to find the House that corresponds to the input. 

At last, we built a webpag to present everthing we obatined so far.


## 6 Refrence 
+  https://www.mapr.com/blog/inside-look-at-components-of--engine
+  http://bigdata.ices.utexas.edu/project/large-scale-recommender-systems/
  
  

