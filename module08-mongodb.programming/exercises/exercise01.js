function gun(numbers){
    return numbers.filter( n => n%2 === 0).map( p => p**3).reduce( (acc,num) => acc+num , 0);
}