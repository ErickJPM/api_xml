import web # pip installl web.py

urls = (
    '/calculadora_xml/?','application.controllers.calculadora_xml.CalculadoraXml'

)
app = web.application(urls, globals())

render = web.template.render('templates/')





if __name__ == "__main__":
    web.config.debug= False
    app.run()