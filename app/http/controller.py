from flask import render_template, flash, redirect

class Controller:
    @staticmethod
    def view(template_name, **option):
        """return view"""
        return render_template(template_name+'.html', **option)

    @staticmethod
    def flash_message(message, category="message"):
        """flash message"""
        return flash(message, category)
        
    @staticmethod
    def redirect_to(location, code=302, response=None):
        """redirect to location"""
        return redirect(location, code, response)
