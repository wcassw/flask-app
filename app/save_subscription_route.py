@app.route('/saveSubscription', methods=['POST'])
def save_subscription():
	
	email = request.form['email']
	book_id = request.form['book_id']
		
	subscription = Subscription(
		email = email,
		book_id = book_id,
		created_at = datetime.datetime.now()
	)
	
	app_db.session.add(subscription)
	app_db.session.commit()
	
	return True
