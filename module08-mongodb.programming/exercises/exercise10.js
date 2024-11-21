db.movies.aggregate([
	{
		$set: {
			"url": { $concat: ["https://www.imdb.com/title/", "$imdb"]}
		}	
	}	
]);