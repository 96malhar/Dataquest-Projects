import read
import pandas as pd

if __name__ == "__main__":
	df=read.load_data()

	df['submission_time'] = pd.to_datetime(df['submission_time'])
	df['hour'] = df['submission_time'].dt.hour
	df['year'] = df['submission_time'].dt.year
	df['day'] = df['submission_time'].dt.day
	df['minute'] = df['submission_time'].dt.minute
	df['weekday'] = df['submission_time'].dt.weekday_name
	

	print(df['hour'].value_counts())
	print(df['weekday'].value_counts())
