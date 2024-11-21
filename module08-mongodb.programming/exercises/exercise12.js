db.movies.aggregate([
	{
		$unwind: {
			"path": "$genres"
		}
	},
	{
		$set: {
		    "genres": "$genres.name"	
		}	
	},
	{
		$group: {
		    "_id": "$genres",
			"count": { $sum: 1 }		
		}	
	},
	{
		$match: {
			"count" : {$gt : 10}
		}
	},
	{
		$sort: {
			count: -1
		}
	},
	
]);