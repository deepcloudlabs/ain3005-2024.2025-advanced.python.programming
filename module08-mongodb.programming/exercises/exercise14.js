db.movies.aggregate([
	{
		$set: {
			"numberOfDirectors": {$size: "$directors"},
			"numberOfGenres": {$size: "$genres"}
		}
	},
	{
		$match:{
			"numberOfDirectors": {$gt: 1}
		}
	}
]);
