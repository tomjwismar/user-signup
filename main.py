import webapp2
import cgi
import re

page_header = """
<!DOCTYPE html>
<html>
<head>
	<title>Sign Up</title>
	<style type="text/css">
		.error {
			color: red;
		}
	</style>
</head>
<body>
	<h1>Signup</h1>
"""

page_footer = """
</body>
</html>
"""

add_form = """
<form method="post">
	<table>
		<tr>
			<td><label for="username">Username:</label></td>
			<td>
				<input name="username" type="text" value="%(e)s" required />
				<span class="error">%(a)s</span>
			</td>
		</tr>
		<tr>
			<td><label for="password">Password:</label></td>
			<td>
				<input name="password" type="password" value="" >
				<span class="error">%(b)s</span>
			</td>
		</tr>
		<tr>
			<td><label for="Verify">Verify Password:</label></td>
			<td>
				<input name="verify" type="password" value="" >
				<span class="error">%(c)s</span>
			</td>
		</tr>
		<tr>
			<td><label for="email">Email (optional):</label></td>
			<td>
				<input name="email" type="email" value="%(f)s">
				<span class="error">%(d)s</span>
			</td>
		</tr>
	</table>
	<input type = "submit" value="Submit">
</form>
"""

welcome_form = """
	<h2>Welcome, %(e)s!</h2>
"""

full_form = page_header + add_form + page_footer
full_welcome = page_header + welcome_form + page_footer

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
	return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
	return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
	return not email or EMAIL_RE.match(email)




class Signup(webapp2.RequestHandler):

	def get(self):
		self.response.write(full_form % {"a": "", "b": "", "c": "", "d": "", "e": "", "f": ""})


	def post(self):
		username_error = False
		password_error = False
		verify_error = False
		email_error = False

		error_username = ""
		error_password = ""
		error_verify = ""
		error_email = ""

		username = self.request.get('username')
		password = self.request.get('password')
		verify = self.request.get('verify')
		email = self.request.get('email')



		if not valid_username(username):
			error_username = "That's not a valid username."
			username_error = True

		if not valid_password(password):
			error_password = "That wasn't a valid password."
			password_error = True

		elif password != verify:
			error_verify = "Your passwords didn't match."
			verify_error = True


		if not valid_email(email):
			error_email = "That's not a valid email."
			email_error = True


		if username_error or password_error or verify_error or email_error:
			username = cgi.escape(username, quote = True)
			email = cgi.escape(email, quote = True)

			self.response.write(full_form % {"a": error_username,"b": error_password,
			"c": error_verify,"d": error_email,"e": username,"f": email})

		else:
			self.redirect('/Welcome?username={}'.format(username))



class Welcome(webapp2.RequestHandler):

	def get(self):
		username = self.request.get('username')
		self.response.write(welcome_form % {'e': username})



app = webapp2.WSGIApplication([
	('/', Signup),
	('/Welcome',Welcome)
], debug=True)
