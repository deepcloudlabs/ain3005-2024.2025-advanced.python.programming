db.countries.aggregate({ 
    $group: { 
	     "_id": "$continent", 
		 "numberOfCountries": { $sum: 1 } 
	} 
});