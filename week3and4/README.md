# Assignment 2 (due 2/18)
> Benzon Carlitos Salazar

## Description

The goal of this project is for you to get familiar with data cleaning, schema matching, and data matching. Each student 
will submit a report (in pdf or google doc format). The report should list the following items: 

1. Recall that in Project 1, you have created two tables tableA.csv and tableB.csv. These two tables should have the same 
schema; that is, they should have the same attributes. If the two tables have different schemas, then transform them to 
have the same schema. List the schema of the two tables. 
2. Let S be the set of attributes in the above table schema. For example, if tables A and B both have the schema 
books(id, title, authors), then S has only three attributes: id, title, and authors. If S has more than 10 attributes, 
then drop attributes from S until S has exactly 10 attributes. You can drop any attributes that you like. List the 
attributes in the set S.
3. For each attribute X in S, consider only Table A and discuss the following in the report: 
	- Missing values: report the percentage of missing values for X. For example, if there are 20 tuples in Table A, but 
	X has value in only 5 of them, then the percentage of missing values for X in Table A is 75%. (Report both the 
	fraction and the percentage.)
	- You often have to fill in these missing values somehow for machine learning in subsequent steps. Discuss solutions 
	you may use to fill in these missing values (you don't have to fill in these values; I'm only asking for a discussion 
	of possible solutions).
	- Classify the attribute X as numeric, textual, categorical, or boolean. If you can't classify, discuss why (e.g., 
	an attribute has values 1, 3, and medium, so it's neither numeric nor categorical).
	- If the attribute X is textual, report the average length of its values, report the minimal and the maximal length 
	of its values (length is measured in the number of characters in the value). 
	- Find and report possible outliers and anomalies among the attribute values. For example, if attribute price 
	typically has values in the range $1-20, and then there is a value of $200, then this value is an outlier and can 
	also be an anomaly (that is, an incorrect value in this case). You can detect outliers by creating a histogram on 
	some property of the attribute values. For example, a histogram on price values will help detect price outliers. As 
	another example, if an attribute is textual, then a histogram on the length of the values (as measured by the number 
	of characters in the value) can help detect very long or short values. Show at least two histograms that you have 
	created (I am not asking for two histograms per attribute; I am just asking for at least two histograms; they could 
	be for two attributes X and Y, for example). 
	- If the attribute value is supposed to follow a certain format (e.g., dates), then discuss if all values follow the 
	same format or if there is some problem with the format, and we will have to standardize the formats later. 
	- Are there synonyms among attribute values? For example, an attribute "book-type" may have values "softcover" and 
	"paperback", which are synonyms. 
	- Sometimes, attribute values are "sprinkled" all over the item. For example, a book may have an attribute "publisher", 
	but its value is missing. Instead, the book title contains the publisher (e.g., "Principles of Data Integration by 
	Springer"). Do you have this problem with this attribute? 
	- Do you see any other data quality problems with this attribute? 
4. List any software tools you have used to understand and clean the above data. For example, if you have used a particular 
Python package, list the name of the package. 

## Deliverables

By the deadline, please put the report in pdf or google doc format on your project's page and provide a link to it. 
