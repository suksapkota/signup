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

import webapp2
import re
import cgi

USER_RE=re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE=re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE=re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>SignUp</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>SignUp</h1>
    """

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        error1 = self.request.get("erroru")
        error2 = self.request.get("errorp")
        error3 = self.request.get("errorv")
        error4 = self.request.get("errore")
        # error_element = "<p class='error'>"+ error + "</p>" if error else ""

        # a form for labeling
        add_form = """
        <form action="/signup" method="post">
        <table>
        <tr>
          <td class ="label">
                Username
            </td>
            <td>
                <input type="text" name="username" value="" required=""/>
            </td>
            <td class ="error">
            {0}
            </td>
            </tr>
            <tr>
            <td class ="label">
                Password
            </td>
            <td>
            <input type="password" name="password" value="" required=""/>
            </td>
            <td class ="error">
            {1}
            </td>
            </tr>
        <tr>
          <td class ="label">
            Verify Password
            </td>
            <td>
            <input type="password" name="verify" value="" required=""/>
        </td>
        <td class ="error">
        {2}
        </td>
        </tr>
        <tr>
        <td class="label">
            Email(Optional)
            </td>
            <td>
            <input type="text" name="email" value=""/>
        </td>
        <td class ="error">
        {3}
        </td>
        </tr>
        </table>
            <input type="submit" value="Submit Query"/>
        </form>
        """.format(error1,error2,error3,error4)

        content=page_header+add_form+page_footer
        self.response.write(content)

welcome_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Page</title>
</head>
<body>
   <h1></h1>
    """

class SignUp(webapp2.RequestHandler):

    def post(self):
        username=self.request.get("username")
        password=self.request.get("password")
        verify=self.request.get("verify")
        email=self.request.get("email")



        if not valid_username(username):
            erroru ="That's not a valid username."
            error_escaped = cgi.escape(erroru, quote=True)
            self.redirect("/?erroru=" + error_escaped)
        elif not valid_password(password):
            errorp="That's not a valid password."
            error_escaped = cgi.escape(errorp, quote=True)
            self.redirect("/?errorp=" + error_escaped)
        elif password!=verify:
            errorv="Your passwords didn't match"
            error_escaped = cgi.escape(errorv, quote=True)
            self.redirect("/?errorv=" +  error_escaped)
        elif not valid_email(email):
            errore="That's not a valid email."
            error_escaped = cgi.escape(errore, quote=True)
            self.redirect("/?errore=" + error_escaped)
        else:
            self.redirect("/welcome?username= "+username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username=self.request.get("username")
        self.response.write(welcome_header+"""<h1>"""+"""Welcome, """+username+"""</h1>"""+page_footer)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup',SignUp),
    ('/welcome',Welcome)
], debug=True)
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.C
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

import webapp2
import re
import cgi

USER_RE=re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE=re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE=re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>SignUp</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>SignUp</h1>
    """

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        error1 = self.request.get("erroru")
        error2 = self.request.get("errorp")
        error3 = self.request.get("errorv")
        error4 = self.request.get("errore")
        # error_element = "<p class='error'>"+ error + "</p>" if error else ""

        # a form for labeling
        add_form = """
        <form action="/signup" method="post">
        <table>
        <tr>
          <td class ="label">
                Username
            </td>
            <td>
                <input type="text" name="username" value="" required=""/>
            </td>
            <td class ="error">
            {0}
            </td>
            </tr>
            <tr>
            <td class ="label">
                Password
            </td>
            <td>
            <input type="password" name="password" value="" required=""/>
            </td>
            <td class ="error">
            {1}
            </td>
            </tr>
        <tr>
          <td class ="label">
            Verify Password
            </td>
            <td>
            <input type="password" name="verify" value="" required=""/>
        </td>
        <td class ="error">
        {2}
        </td>
        </tr>
        <tr>
        <td class="label">
            Email(Optional)
            </td>
            <td>
            <input type="text" name="email" value=""/>
        </td>
        <td class ="error">
        {3}
        </td>
        </tr>
        </table>
            <input type="submit" value="Submit Query"/>
        </form>
        """.format(error1,error2,error3,error4)

        content=page_header+add_form+page_footer
        self.response.write(content)

welcome_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Page</title>
</head>
<body>
   <h1></h1>
    """

class SignUp(webapp2.RequestHandler):

    def post(self):
        username=self.request.get("username")
        password=self.request.get("password")
        verify=self.request.get("verify")
        email=self.request.get("email")



        if not valid_username(username):
            erroru ="That's not a valid username."
            error_escaped = cgi.escape(erroru, quote=True)
            self.redirect("/?erroru=" + error_escaped)
        elif not valid_password(password):
            errorp="That's not a valid password."
            error_escaped = cgi.escape(errorp, quote=True)
            self.redirect("/?errorp=" + error_escaped)
        elif password!=verify:
            errorv="Your passwords didn't match"
            error_escaped = cgi.escape(errorv, quote=True)
            self.redirect("/?errorv=" +  error_escaped)
        elif not valid_email(email):
            errore="That's not a valid email."
            error_escaped = cgi.escape(errore, quote=True)
            self.redirect("/?errore=" + error_escaped)
        else:
            self.redirect("/welcome?username= "+username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username=self.request.get("username")
        self.response.write(welcome_header+"""<h1>"""+"""Welcome, """+username+"""</h1>"""+page_footer)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup',SignUp),
    ('/welcome',Welcome)
], debug=True)
