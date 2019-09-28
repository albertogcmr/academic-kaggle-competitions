# Kaggle competition

Cars competition datamad0819

## 1. Overview

### 1.1. Timeline

06/10/2019 a las 23:59

### 2. Prices

No prices

### 3. Kernel Requirements

None

### 4. Description

Dataset description text



## 2. Data

### 2.1. Competition description

The goal of this competition is the **prediction** of car prices based on their characteristics.

### 2.2. Files description
You will find three files:

- **car_train**: This is a file with the the all the car information and their price. You will train your model with it.

- **car_test**:  This is a file with all the information but the price which you will have to predict. 

- **sample_submission**:  This is just an example of the submission you have to upload.

_________________________________

⚠️ You are only allowed to upload 5 submissions per day. Make every submission count. 

⚠️ Remember the characteristics of the submissions (the type of model you have used and its score). Before finishing the competition, you can choose two final submissions, which you consider to have better results.

_________________________________

### 2.3. Columns description



- Id (str)
- city
- price
- year: Year of manufacturing
- manufacturer: Manufacturer of vehicle
- make: Model of vehicle
- condition: Vehicle condition
- cylinders: Number of cylinders
- fuel: Type of fuel required
- odometer: Miles traveled
- title_status: Title status (e.g. clean, missing, etc.)
- transmission: Type of transmission
- drive: Drive of vehicle
- size: Size of vehicle
- type: Type of vehicle
- paint_color: Color of vehicle
- lat: Latitude of listing
- long: Longitude of listing
- county_fips: Federal Information Processing Standards code
- county_name: County of listing
- state_fips: Federal Information Processing Standards code
- state_code: letter state code
- state_name: State name
- weather: Historical average


This is an academic competition created for the students of Iron Hack Data Analytics Bootcamp 0819.


## 3. Rules


- Don't cheat!
- Apply yourself!
- Have fun!

## 4. Host

### 4.1. Settings

1. Teams: No teams enabled
2. Maximum Daily Submissions: 5
3. Scored Private Submissions: 2

### 4.2 Evaluation

1. Scoring Metric: RMSE (Root Mean Squared Error)
2. Solution File: Real solution. Id + real target of every element in sample_submission
3. Solution Mapping: Id (string), price (Expected Double)
4. Public Leaderboard Percentage: 30. 70% of predictions will be hidden until the end. 
5. Sample Submission: example of submission
6. Sample Mapping: To test possible submission