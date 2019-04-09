import read
import pandas as pd



if __name__ == "__main__":
	df=read.load_data()
	df["head_len"]=df["headline"].str.len()

	head_len_upvotes = df.groupby('head_len')["upvotes"].mean()
	print("Max Upvotes =",head_len_upvotes.max())	
	print("Headline length =",head_len_upvotes.idxmax())

	
	df['submission_time'] = pd.to_datetime(df['submission_time'])
	df['hour'] = df['submission_time'].dt.hour
	hour_upvotes = df.groupby('hour')['upvotes'].mean()
	print('Max_upvotes =',hour_upvotes.max())
	print('Time =',hour_upvotes.idxmax())
	
	
	
