import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\Despr\OneDrive\Desktop\accidents_new.csv.txt")


df.columns = df.columns.str.strip().str.lower()


print("Cleaned columns:", df.columns)


if 'date_time' in df.columns:
    df['date_time'] = pd.to_datetime(df['date_time'])
else:
    raise KeyError("Column 'date_time' not found in dataset")


df['hour'] = df['date_time'].dt.hour


road_condition_counts = df['road_condition'].value_counts()
print("Accidents by Road Condition:")
print(road_condition_counts)


weather_condition_counts = df['weather_condition'].value_counts()
print("Accidents by Weather Condition:")
print(weather_condition_counts)


collision_type_counts = df['collision_type'].value_counts()
print("Accidents by Collision Type:")
print(collision_type_counts)


severity_counts = df['accident_severity'].value_counts()
print("Accidents by Severity:")
print(severity_counts)


hourly_accidents = df['hour'].value_counts().sort_index()
print("Accidents by Hour of Day:")
print(hourly_accidents)


plt.figure(figsize=(18, 8))


plt.subplot(2, 3, 1)
sns.barplot(x=road_condition_counts.index, y=road_condition_counts.values, palette='viridis')
plt.title('Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')


plt.subplot(2, 3, 2)
sns.barplot(x=weather_condition_counts.index, y=weather_condition_counts.values, palette='viridis')
plt.title('Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')


plt.subplot(2, 3, 3)
sns.barplot(x=collision_type_counts.index, y=collision_type_counts.values, palette='viridis')
plt.title('Accidents by Collision Type')
plt.xlabel('Collision Type')
plt.ylabel('Number of Accidents')


plt.subplot(2, 3, 4)
sns.barplot(x=severity_counts.index, y=severity_counts.values, palette='viridis')
plt.title('Accidents by Severity')
plt.xlabel('Severity')
plt.ylabel('Number of Accidents')


plt.subplot(2, 3, 5)
sns.lineplot(x=hourly_accidents.index, y=hourly_accidents.values, marker='o')
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')

plt.tight_layout()
plt.show()
