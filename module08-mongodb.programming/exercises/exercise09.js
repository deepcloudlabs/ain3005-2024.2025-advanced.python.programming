db.countries.aggregate([
	{
		$set: {
			"populationPerArea": {$cond: {if: {"$eq": ["$surfaceArea", 0]}, then: undefined, else: {$divide: ["$population", "$surfaceArea"]}}}
		}	
	},
	{
		$match : {
			"populationPerArea" : {$lt: 100}
		}	
	},
	{
		$project: {
			"name": "$name",
			"population": "$population",
			"populationPerArea": "$populationPerArea",
			"surfaceArea": "$surfaceArea",
			"continent": "$continent"
		}
	}	
]);