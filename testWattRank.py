from wattRankCluster import genClusters
from wattRankCluster import makePrediction

model, modelFit, data, totaldol = genClusters();
ranking, dollar_ranks = makePrediction(model, modelFit, data, totaldol, 5, 800, 20, 1200);

print "Your electricity usage is ranked " + str(ranking) + " out of " + str(len(dollar_ranks)) + " similar users"; 








