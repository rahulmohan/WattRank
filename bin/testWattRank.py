from wattRankCluster import genClusters
from wattRankCluster import makePrediction

print "Training clustering model...\n"
model, modelFit, data, totaldol = genClusters();

div = raw_input("Enter your Census Division (1..10): ");
sqft = raw_input("Enter the Total Square Feet of your Home: ");
income = raw_input("Enter income range (1..20): ");
bill = raw_input("Enter energy bill in dollars for the past year: ");

ranking, dollar_ranks, shouldBeAmount, highestVal, lowestVal = makePrediction(model, modelFit, data, totaldol, int(div), int(sqft), int(income), int(bill));

print "\nYour electricity usage is ranked " + str(ranking) + " out of " + str(len(dollar_ranks)) + " similar people";
print "The average electricity bill among similar people: " + "$" + str(shouldBeAmount);
print "The lowest electricity bill among similar people: " + "$" + str(lowestVal);
print "The highest electricity bill among similar people: " + "$" + str(highestVal) + "\n";








