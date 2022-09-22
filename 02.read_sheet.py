wb = gc.open_by_url('your_google_sheet_url')
sheet = wb.worksheet('your_sheet_name')
data = sheet.get_all_values()
df = pd.DataFrame(data)
df.columns = df.iloc[0]
df = df.iloc[1:]
df.head()
