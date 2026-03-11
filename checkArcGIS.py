import pandas as pd
from pathlib import Path

semesters = ['Spring2025','Summer2025','Fall2025']
usernames = []
connections = 0

for semester in semesters:
    print(f"--------- {semester} -------------")
    # linux
    #dir_path = Path(f"/home/ed/OneDrive/Virtual Labs/SemesterUsageReports/{semester}/concurrentsessions/")
    # windows
    dir_path = Path(f"C:\\Users\\ed1013.AD\\OneDrive - Boston University\\Virtual Labs\\SemesterUsageReports\\{semester}\\concurrentsessions")
    xlsx_files = list(dir_path.glob("*.xlsx"))
    
    for xlfile in xlsx_files:
        print(xlfile.stem)
        df = pd.read_excel(xlfile, sheet_name="Number of Concurrent Sessions")

        sets = df.iloc[41:, 6]
        strings = [r"Remote Apps\met-azure-remoteapps-gpu",r"Remote Apps\met-az-ArcGIS-vlab"]
        mask  = sets.isin(strings)

        matched_rows = df.iloc[41:][mask]

        # +2 is common when row 1 is header and pandas index starts at 0
        matched_rows.insert(0, "ExcelRow", matched_rows.index + 2)
        #print(matched_rows.iloc[:,[0]+list(range(5, 9))])

        connections += mask.sum()
        print(f"connections: {mask.sum()}")

        user_col = matched_rows.iloc[:,5] # 5 is the index for the username column
        usernames += user_col.tolist() 
        usernames = list(dict.fromkeys(usernames))

        print(f"unique users: {user_col.nunique()}")

        #print(f"list of unique users and connections: {user_col.value_counts()}")

print("----------------Final count: ")
print(f"connections: {connections}\nunique users: {len(usernames)}")