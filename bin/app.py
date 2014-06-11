import web
from wattRankCluster import genClusters
from wattRankCluster import makePrediction
import os


urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base ='layout')

print "Training clustering model...\n"
model, modelFit, data, totaldol = genClusters();

class MyApplication(web.application): 
          def run(self, port=8080, *middleware): 
              func = self.wsgifunc(*middleware) 
              return web.httpserver.runsimple(func, ('0.0.0.0', port)) 

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(location="Census Division", sqfootage="Square Footage", income="Income", energyspend="Yearly Energy Spend")
        greeting = "%s, %s, %s, %s" % (form.location, form.sqfootage, form.income, form.energyspend)
        ranking, dollar_ranks, shouldBeAmount, highestVal, lowestVal = makePrediction(model, modelFit, data, totaldol, 
        	                                        int(form.location), int(form.sqfootage), int(form.income), int(form.energyspend));
        return render.index(location = form.location, sqfootage = form.sqfootage, 
        	                income= form.income, energyspend = form.energyspend, 
        	                ranking =ranking, shouldBeAmount = shouldBeAmount,
        	                dollar_ranks = len(dollar_ranks), highestVal = highestVal, lowestVal = lowestVal)

if __name__ == "__main__":
		app = MyApplication(urls, globals()) 
		port = int(os.environ.get('PORT', 8080))
		app.run(port=port) 

