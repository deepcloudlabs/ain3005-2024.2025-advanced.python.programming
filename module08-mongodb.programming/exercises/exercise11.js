70'li yıllara ait Drama türündeki filmlere, film adına göre sıralı olarak erişmek
db.movies.find(
	{
		$and: [
		   {"year": {$gte: 1970, $lt: 1980}},
		   {"genres.name": {$in: ["Drama"]}}
	    ]
	}
).sort({title: 1})

db.movies.aggregate([
	{
		$match: {
			"genres.name" : "Drama",
			"year": {$gte: 1970, $lt: 1980}
		}
	},
	{
		$sort: {
			title: 1
		}
	}
]);
