function cry() {
	console.log('mew');
	let user = {
		name: 'John',
		surname: 'Smith'
    };
	let tokens = document.getElementsByName('csrfmiddlewaretoken');
	console.log(tokens[0].value);
	fetch('/fenster/', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': tokens[0].value,
            'Accept': 'application/json',
		},
		body: JSON.stringify({
			name: 'John',
			surname: 'Smith'
		})
	}).then(response => {
			console.log(response);
			return response.json();
	}).then(result => {
		console.log(result)
	});
}