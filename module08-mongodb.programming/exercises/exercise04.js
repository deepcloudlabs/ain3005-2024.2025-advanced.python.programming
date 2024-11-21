db.countries.aggregate({ 
    $group: { 
	     "_id": "$continent", 
		 "countries": { $push: "$name" } 
	} 
});