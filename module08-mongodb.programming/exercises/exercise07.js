db.countries.aggregate([
    { 
       $group: { 
	        "_id": "$continent", 
		    "numberOfCountries": { $sum: 1 },
		    "numberOfCities": { $sum: {$size: "$cities"} } 
	    } 
	},
	{
		$set: {
			"avgNumberOfCities": {$divide: ["$numberOfCities", "$numberOfCountries"]}
		}	
	}	
]);