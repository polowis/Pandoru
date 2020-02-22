from flask import render_template, flash, redirect

class Controller:
    def view(self, template_name, **option):
        """return view"""
        return render_template(template_name+'.html', **option)

    def flash_message(self, message, category="message"):
        """flash message"""
        return flash(message, category)
    
    def redirect_to(self, location, code=302, response=None):
        """redirect to location"""
        return redirect(location, code, response)
