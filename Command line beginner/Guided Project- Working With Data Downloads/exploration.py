
if __name__ == "__main__":
	
	import pandas as pd
	import numpy as np
	data=pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")
		
	
	print(data["JJ"].value_counts())
	print(data["SCH_STATUS_MAGNET"].value_counts())

	pivot_jj=data.pivot_table(index='JJ',values=['TOT_ENR_M','TOT_ENR_F'],aggfunc=np.sum)
	pivot_sch_status=data.pivot_table(index='SCH_STATUS_MAGNET',values=['TOT_ENR_M','TOT_ENR_F'],aggfunc=np.sum)
    
	print(pivot_jj)
	print(pivot_sch_status)
