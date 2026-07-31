# ...........Fake Profile Detection using Machine Learning............

## 📌 Overview
Fake social media profiles are widely used for online scams, spreading misinformation, and cybercrime. These fake accounts often have unusual behavior patterns such as very low follower counts, abnormal following ratios, fewer posts, or incomplete profile information.

This project focuses on detecting **fake vs genuine social media profiles** using **Machine Learning techniques** by analyzing basic profile-level features. The system predicts whether a given profile is fake or genuine based on trained data.

---

## 🎯 Problem Statement
With the rapid growth of social media platforms, the number of fake profiles has increased significantly. Manual identification of fake accounts is time-consuming and inefficient.

The objective of this project is to:
- Automatically detect fake profiles
- Reduce online fraud and impersonation
- Improve trust and safety on social media platforms

---

## 💡 Proposed Solution
We use a **supervised machine learning approach** where a model is trained on labeled profile data. The trained model learns patterns that distinguish fake profiles from genuine ones and predicts the authenticity of new profiles.

---

## 🏗️ System Architecture
Input Dataset (CSV)
↓
Feature Extraction
↓
Machine Learning Model
↓
Prediction (Fake / Genuine)


---

## 📊 Dataset Description
A custom dataset is created for demonstration purposes.

### Features used:
| Feature Name | Description |
|--------------|-------------|
| followers | Number of followers |
| following | Number of accounts followed |
| posts | Number of posts |
| bio_length | Length of profile bio |
| is_fake | Target label (1 = Fake, 0 = Genuine) |

The dataset is stored in `profiles.csv`.

---

## 🧪 Machine Learning Model
- **Algorithm Used:** Logistic Regression  
- **Type:** Binary Classification  
- **Reason for selection:**
  - Simple and efficient
  - Works well for small datasets
  - Easy to interpret

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📂 Project Structure
fake-profile-detection/
│
├── profiles.csv # Dataset
├── fake_profile_model.py # Model training script
├── predict.py # Prediction script
├── fake_profile_model.pkl # Saved trained model
├── README.md # Project documentation


---

## ▶️ How to Run the Project

### Step 1: Install required libraries

pip install pandas scikit-learn joblib

### Step 2: Train the model

python fake_profile_model.py

This will:
- Train the model
- Display accuracy
- Save the trained model as `fake_profile_model.pkl`

---

### Step 3: Predict profile authenticity
python predict.py

Sample Output:
Fake Profile or Genuine Profile

---

## 📈 Results
The model successfully classifies profiles as fake or genuine based on input features. Even with a simple dataset, the system demonstrates the effectiveness of machine learning in detecting suspicious profiles.

---

## 🚀 Future Enhancements
- Use a larger real-world dataset
- Add features like account age, activity frequency, and profile picture analysis
- Improve accuracy using advanced ML algorithms
- Integrate with a web or mobile application
- Deploy model using Flask or FastAPI

---

## 🌍 Impact
This project helps in:
- Reducing online fraud
- Improving user trust on social platforms
- Supporting safer digital communities

---

## 👩‍💻 Author
**Saranya S**  
3rd Year Student  
India AI Impact Buildathon Participant

---

## 📜 License
This project is developed for educational and hackathon purposes.
