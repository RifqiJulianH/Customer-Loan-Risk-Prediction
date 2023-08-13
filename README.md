# Customer Loan Default Prediction

## Table of Contents
- [Introduction](#introduction)
- [Objective](#objective)
- [Getting Started](#getting-started)
- [Data](#data)
- [Model](#model)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This repository contains a predictive modeling project aimed at predicting customer loan defaults for a bank in Indonesia. The goal is to develop a predictive model that can assess the likelihood of a customer failing to make loan payments based on historical customer behavior data.

## Objective
The main objectives of this project are:
1. Build a predictive model for customer loan default prediction.
2. Gain insights into customer behavior based on the provided dataset.

## Getting Started
To run the project locally, follow these steps:
1. Clone this repository: `git clone https://github.com/your-username/customer-loan-default.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`

## Data
The dataset used for this project contains historical customer behavior data, including features such as salary, marital status, profession, etc. The dataset is available in the `data.csv` file.

## Model
The predictive model is based on a Decision Tree algorithm. It is trained on the historical customer behavior data to predict the likelihood of loan defaults.

## Usage
The main components of this repository are:
- `app.py`: Streamlit app for interactive usage of the predictive model.
- `data.csv`: Dataset containing historical customer behavior data.
- `FinalProject.pkl`: Pre-trained Decision Tree model saved using joblib.

## Results
The Decision Tree model achieved an accuracy of approximately 86% in predicting loan defaults. The insights gained from the model can help the bank identify high-risk customers and make informed decisions to manage credit risk.

## Contributing
Contributions are welcome! If you find any issues or want to enhance the project, feel free to submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
