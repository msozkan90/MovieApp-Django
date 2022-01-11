var ratingbutton = document.getElementsByClassName('starbar')
var rating_value = document.getElementsByClassName('rating_value')

var rate_list = []


for (i = 0; i < ratingbutton.length; i++) {
	ratingbutton[i].addEventListener('click', function (e) {
		var rating = this.dataset.product
		var user = this.dataset.user
		var film = this.dataset.film
		var avg=this.dataset.rate
		console.log(avg)

		if (user == 'AnonymousUser') {
			console.log("çalışmadı")
		} else {
			var rate1 = 0
			var rate = 0

			rating = Number(rating)
			rate_list.push(rating)
			for (let i in rate_list) {
				
				rate += rate_list[i];
				rate1 = (rate / rate_list.length)
			}


			
			setratesToLS(rating, rate1, user, rate_list,film,avg)
		}

		//e.preventDefault();
	})


}

/*------------------------------------------------------------------------------------*/
/*------------------------------------------------------------------------------------*/


// get items from Local Storage
function getRatesFromLS() {
	if (localStorage.getItem('rates') !== null) {
		rates = JSON.parse(localStorage.getItem('rates'));
	} else {
		rates = []
	}
	return rates;
}

var user_list=[]

var durum=0
function setratesToLS(rating, rate1, user, rate_list,film,avg) {
	rates = getRatesFromLS();
	

	if (localStorage.getItem('rates') !== null) {
		for(i in rates){
			if (user == rates[i][1] && film == rates[i][0]){
				
				durum=1
			}
			else{
				console.log("Item was add")
			}
		}
		if(durum !== 0){
			durum=0
			console.log("same")
			at= localStorage.getItem('rates')
			console.log(at)
		}
		else{
			rates.push([film,String(user), rating]);
			localStorage.setItem('rates', JSON.stringify(rates));			
			addRatetoFilm(user,rating,film,avg)

		}

	} 
	else{
		rates.push([film,String(user), rating]);
		localStorage.setItem('rates', JSON.stringify(rates));
		addRatetoFilm(user,rating,film,avg)
	}

	for (i in rates){
		console.log(rates[i])
	}


}






function addRatetoFilm(user, rate,film,avg){
	console.log('User is authenticated, sending data...')

		var url = '/add_rate/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'film':film, 'user':user ,'rate':rate,'avg':avg}),
			// body:JSON.stringify({'film':film, 'user':user ,'rate':rate,'avg':avg})
		})
		.then((response) => {
			return response.json();
		 })
		 .then((data) => {
				 parent.location.reload()
			 console.log(data)
		 });
}

