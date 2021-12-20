# Data_Mgmt_final-
  The nascence of this project idea stems from my general interest in sex work, from both a
legal lens and a cultural sense. Through modes of pattern identification following many years of
consuming media related to the topic, I realized that if one were to analyze the movement of
prostitution arrests in a post-Giuliani world, a pattern might emerge. By combining qualitative
and quantitative data analysis, I utilized the following methods to illustrate a direct relationship
between the city’s changing political landscape and the concentration of prostitution arrests in
commercialized areas of Manhattan.
  In order to paint a clear picture of how legislation affects the lives of sex workers in New
York City, this project utilizes arrest data from NYC Open Data and both civil and criminal case
data from the Caselaw Access Project. Below are the various methods used to pull and parse data
from both aforementioned repositories:

  1. Utilize the Caselaw Access Project API (CAPAPI) to pull cases specific to charges of
prostitution beginning in 1970 with varying degrees and New York State Penal Law
references. The use of the API is necessary, as the API serves all official US court cases
published in books from 1658 to 2018. The collection includes over six million cases
scanned from the Harvard Law School Library shelves. After utilizing the API, I created
an interactive timeline hosted by CAP that correlates with relevant events such as
mayoral terms, legislation passing, and the chronology of the development plan that
changed Times Square forever. 
  *The files related to this step include the code, "Case_API.py", and the result of the code, "Case_API_Results.json" 
  2. Use Python to parse through the CSV file downloaded from NYC Open Data to pull data
only relating to charges of prostitution. Following this first step were various parsing and
looping iterations to find data specific to an arrest year or borough for visualization
purposes. Unfortunately, the only available historic arrest data on NYC Open Data range
from 2006 to the present day. I requested the institution’s team for data from the 1970s
onward, but the team did not have those records available. After creating a useable,
narrowed dataset, I created an interactive map visualization in Tableau.
  *The files related to this step include the original NYC Open Data file "Arrests.csv" , the code used to parse this file "Borough_Offense_parse.py" and the resulting files "Queens_arrests.csv" , "Manhattan_arrests.csv" , "Bronx.arrests.csv" , "Brooklyn_arrests.csv" , and "Staten_arrests.csv" 
  3. While heavy in data analysis and code usage, a large portion of this project demanded
extensive research into the legislation and political occurrences during the time frame of
my project scope. An analysis of Article 230 in the New York State Penal Law was
essential here, as this section of the law deals entirely with charges of prostitution.
Additionally, although not within Article 230, section 240.37 of the law is relevant here
as it is an anti-loitering law for the “purposes of engaging in a prostitution offense.”
Additionally, I referenced a multitude of literature relating to the topic, ranging from
news articles to scholarly journals, to understand the legal and cultural pulse regarding
sex work through the decades.

Please feel free to reach out to me if you have questions about recreating this project and/or need clarifications with the coding. 
