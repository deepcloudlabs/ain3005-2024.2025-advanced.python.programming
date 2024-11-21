db.movies.aggregate([
	{
		$unwind: {
			"path" : "$directors"
		}
	},
	{
		$group: {
			"_id": { 
				"imdb": "$directors.imdb", 
				"name": "$directors.name",
				"url": { $concat: ["https://www.imdb.com/name/", "$directors.imdb"]}
			},
			"movies": {$push: {title: "$title", "url": { $concat: ["https://www.imdb.com/title/", "$imdb"]}}}
		}
	},
	{
		$set: {
			"name": "$_id.name",
			"url": "$_id.url",
			"_id": "$_id.imdb"
		}
	}
]);
