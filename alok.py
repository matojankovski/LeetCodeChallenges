##### V.V #####

from selenium import webdriver
from openpyxl.workbook import Workbook
import pandas as pd

driver = webdriver.Chrome()
driver.get('http://smbtv419/ads.php?menuid=vyrobaosoby&osoba=8188111&obdobi=1.7.2023') #TODO: zadej vlastní adresu: Alokace na zakázky měsíční (Z hlavní stránky)

driver
date = []
time = []
work = []
projects = []

for project in range(0, 5):                       
    try:
        row_index = driver.find_elements("xpath", f'/html/body/div[6]/div[1]/div[2]/form[2]/div/table/tbody[1]/tr[{project}]/td[2]') # tbody[2] - pokud je docházka schválená
        for i in range(0, 33):              
            work_days = driver.find_elements("xpath", f'/html/body/div[6]/div[1]/div[2]/form[2]/div/table/tbody[1]/tr[{project}]/td[{i+3}]/input[1]') #tbody[2] - pokud je docházka schválená
            
            try:
                if work_days[0].get_attribute("value") != "":
                    date.append(work_days[0].get_attribute("data-datum"))
                    time.append(work_days[0].get_attribute("value"))
                    work.append(work_days[0].get_attribute("title"))
                    projects.append(row_index[0].text)
            except:
                pass # pro rozdílný počet dnů v měsíci.
    except:
        pass
    
data_tuples = list(zip(date, time, work, projects))
temp_df = pd.DataFrame(data_tuples, columns=["Datum", "Odpracováno", "Alokace", "Projekt"])
temp_df.to_excel(r"c:\Users\martin.jankovsky\Documents\dochazka_new.xlsx", sheet_name="Docházka", index=False) # Zadej cestu, kde se má uložit soubor.(name = jmeno.prijmeni)

driver.close()

