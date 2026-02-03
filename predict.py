import joblib

model = joblib.load("fake_profile_model.pkl")

profile = [[50, 500, 5, 10]]  # followers, following, posts, bio_length

result = model.predict(profile)

print("Fake Profile" if result[0] == 1 else "Genuine Profile")
