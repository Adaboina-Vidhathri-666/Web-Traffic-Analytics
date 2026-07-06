import pandas as pd

# Load dataset
df = pd.read_csv("web_traffic.csv")

print("WEB TRAFFIC ANALYTICS")
print("=" * 40)

print("\nDataset:")
print(df)

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nTotal Visitors")
print(len(df))

print("\nAverage Page Views")
print(df["PageViews"].mean())

print("\nAverage Session Duration (seconds)")
print(df["SessionDuration"].mean())

print("\nTraffic Sources")
print(df["TrafficSource"].value_counts())

print("\nMost Visited Pages")
print(df["Page"].value_counts())

print("\nDevice Usage")
print(df["Device"].value_counts())

print("\nBounce Rate")
print(df["Bounce"].value_counts())

print("\nConversions")
print(df["Conversion"].value_counts())

# Drop-off users
drop_off = df[df["Bounce"] == "Yes"]

print("\nDrop-off Users")
print(drop_off)

# Highly Engaged Users
engaged = df[
    (df["SessionDuration"] > 300) &
    (df["PageViews"] > 7)
]

print("\nHighly Engaged Users")
print(engaged)

# Save reports
drop_off.to_csv("drop_off_users.csv", index=False)
engaged.to_csv("engaged_users.csv", index=False)

print("\nAnalysis Completed Successfully!")