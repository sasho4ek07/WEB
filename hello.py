def app(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]	
	strings = environ['QUERY_STRING'].split('&')
    	body = [string+"\n" for string in strings]
	start_response(status, headers)
	return body

