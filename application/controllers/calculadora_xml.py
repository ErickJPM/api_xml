import web
import app
import json
render = web.template.render('application/views/')
class CalculadoraXml:
    def GET(self):
        form=web.input()
        num1=int(form['num1'])
        num2=int(form['num2'])

        add= num1+num2
        substraction=num1-num2
        web.header('Content-Type','text/xml')
        return render.calculadora_xml(add,substraction)
