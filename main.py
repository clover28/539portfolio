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
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" href=\"style_sheets/reset.css\"><link rel=\"stylesheet\" href=\"style_sheets/style.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><script src=\"js/modernizr.js\"></script>"
        script = "<script src=\"js/jquery-2.1.1.js\"></script><script src=\"js/jquery.mixitup.min.js\"></script><script src=\"js/main.js\"></script>"
        template_vars = {
            'style': style,
            'script': script,
            'name':'index'
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(template_vars))

class workHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\">"
        script = ""
        template_vars = {
            'style': style,
            'script': script,
            'name': 'work'
        }
        template = JINJA_ENVIRONMENT.get_template('work.html')
        self.response.out.write(template.render(template_vars))

class galleryHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheetGallery.css\"><link href=\"style_sheets/lightbox.css\" rel=\"stylesheet\"><script>lightbox.option({\"alwaysShowNavOnTouchDevices\": true})</script>"
        script = "<script src=\"js/lightbox-plus-jquery.js\"></script>"
        template_vars = {
            'style': style,
            'script': script,
            'name':'gallery'
        }
        template = JINJA_ENVIRONMENT.get_template('gallery.html')
        self.response.out.write(template.render(template_vars))

class DragonHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><link href=\"https://fonts.googleapis.com/css?family=Abril+Fatface\" rel=\"stylesheet\">"
        script = ""
        template_vars = {
            'style': style,
            'script': script,
            'name': 'work'
        }
        template = JINJA_ENVIRONMENT.get_template('Dragon.html')
        self.response.out.write(template.render(template_vars))

class HaleyHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><link href=\"https://fonts.googleapis.com/css?family=Abril+Fatface\" rel=\"stylesheet\">"
        script = ""
        template_vars = {
            'style': style,
            'script': script,
            'name':'work'
        }
        template = JINJA_ENVIRONMENT.get_template('Haley.html')
        self.response.out.write(template.render(template_vars))

class SI501Handler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><link href=\"https://fonts.googleapis.com/css?family=Abril+Fatface\" rel=\"stylesheet\">"
        script = ""
        template_vars = {
            'style': style,
            'script': script,
            'name':'work'
        }
        template = JINJA_ENVIRONMENT.get_template('501.html')
        self.response.out.write(template.render(template_vars))

class APIHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><link href=\"https://fonts.googleapis.com/css?family=Abril+Fatface\" rel=\"stylesheet\">"
        script = ""
        template_vars = {
            'style': style,
            'script': script,
            'name':'work'
        }
        template = JINJA_ENVIRONMENT.get_template('APIMashup.html')
        self.response.out.write(template.render(template_vars))

class beautyHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheetGallery.css\"><link href=\"https://fonts.googleapis.com/css?family=Abril+Fatface\" rel=\"stylesheet\">"
        script = ""
        template_vars = {
            'style': style,
            'script': script,
            'name':'work'
        }
        template = JINJA_ENVIRONMENT.get_template('beautyOrganizer.html')
        self.response.out.write(template.render(template_vars))

class HyechoHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheetGallery.css\"><link href=\"https://fonts.googleapis.com/css?family=Abril+Fatface\" rel=\"stylesheet\">"
        script = ""
        template_vars = {
            'style': style,
            'script': script,
            'name':'work'
        }
        template = JINJA_ENVIRONMENT.get_template('Hyecho.html')
        self.response.out.write(template.render(template_vars))


class designJamsHandler(webapp2.RequestHandler):
    def get(self):
        style = "<link rel=\"stylesheet\" type=\"text/css\" href=\"style_sheets/myStyleSheet.css\"><link href=\"https://fonts.googleapis.com/css?family=Abril+Fatface\" rel=\"stylesheet\">"
        script = ""
        template_vars = {
            'style': style,
            'script': script,
            'name':'work'
        }
        template = JINJA_ENVIRONMENT.get_template('designJams.html')
        self.response.out.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/work', workHandler),
    ('/gallery', galleryHandler),
    ('/Dragon', DragonHandler),
    ('/Haley', HaleyHandler),
    ('/SI501', SI501Handler),
    ('/API', APIHandler),
    ('/beauty', beautyHandler),
    ('/Hyecho', HyechoHandler),
    ('/designJams', designJamsHandler),
    ('.*', MainHandler)
], debug=True)
