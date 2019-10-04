## 1. Introduction ##

world_dev = pd.read_csv("World_dev.csv")
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
merged = pd.merge(left=happiness2015, right=world_dev, how='left', left_on=happiness2015['Country'], right_on=world_dev['ShortName'])
merged.rename(col_renaming, axis=1, inplace=True)

## 2. Using Apply to Transform Strings ##

def extract_last_word(element):
    last_word = str(element).split()[-1]
    return last_word

merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)
print(merged['Currency Apply'].head())

## 3. Vectorized String Methods Overview ##

merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)
print(merged['Currency Vectorized'].head())