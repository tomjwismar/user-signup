#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #add a form for user input "sign up"
        add_form = """
        <form action="/submit" method="post">
            <table>
                <tr>
                    <td><label for="username">Username:</label></td>
                    <td>
                        <input name="username" type="text" value="" required>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password:</label></td>
                    <td>
                        <input name="password" type="text" value="" required>
                    </td>
                </tr>
                <tr>
                    <td><label for="v_password">Verify Password:</label></td>
                    <td>
                        <input name="v_password" type="text" value="" required>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email(optional):</label></td>
                    <td>
                        <input name="email" type="text" value="">
                    </td>
                </tr>
            </table>
            <input type = "submit" value="Submit">
        </form>
        """
        self.response.write(page_header + add_form + page_footer)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
