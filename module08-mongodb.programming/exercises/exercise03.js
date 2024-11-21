const asian_countries = db.countries.find({"continent": "Asia"},{"name": true});
for( const country of asian_countries){
   printjson(country);
}