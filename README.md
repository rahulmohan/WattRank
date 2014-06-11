WattRank
========

A web application that ranks users based on their energy usage with "similar" users, utilizing machine learning clustering algorithms. Currently takes into account square footage of home, income, and region of the country where you live, to rank you among your similar peers by your energy bill.

Requirements:

```html
web.py
scikit-learn
numpy
scipy
```

How to Run:

```html
git clone https://github.com/rahulmohan/WattRank
cd WattRank
python bin/app.py
```

Then open up your browser to the address the app directs you to.

Additionally, check out WattRank-Readme.docx for more documentation on the code and algorithms being used.

Data Description and Link
========

The data being used is the RECS 2009 survey data. Find out more about it at the following link:
http://www.eia.gov/consumption/residential/data/2009/index.cfm?view=characteristics
