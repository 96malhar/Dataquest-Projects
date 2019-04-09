
if __name__ == "__main__":
	
	import pandas as pd
	import re
	import numpy as np
	data=pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")
		
	
	data['total_enrollments'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
	print(data[['TOT_ENR_M','TOT_ENR_F']].sum()/data['total_enrollments'].sum())

	
	cols = ['SCH_ENR_HI_M',
		 'SCH_ENR_HI_F',
		 'SCH_ENR_AM_M',
		 'SCH_ENR_AM_F',
		 'SCH_ENR_AS_M',
		 'SCH_ENR_AS_F',
		 'SCH_ENR_HP_M',
		 'SCH_ENR_HP_F',
		 'SCH_ENR_BL_M',
		 'SCH_ENR_BL_F',
		 'SCH_ENR_WH_M',
		 'SCH_ENR_WH_F',
		 'SCH_ENR_TR_M',
		 'SCH_ENR_TR_F']

	print(data[cols].sum()/data['total_enrollments'].sum())
