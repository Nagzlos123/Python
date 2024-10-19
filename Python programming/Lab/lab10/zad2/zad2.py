import uno
def my_first_macro_writer():
    doc = XSCRIPTCONTEXT.getDocument()  
    text = doc.getText()  # com.sun.star.text.Text 
    text.setString('Hello World in Python in Writer') 
    return

import uno
def my_first_macro_calc(): 
    doc = XSCRIPTCONTEXT.getDocument()
    cell = doc.Sheets[0]['A1']
    #
    com.sun.star.sheet.XSpreadsheetDocument  
    cell.setString('Hello World in Python in Calc') 
    return

import uno 
def hello_world():
    context = uno.getComponentContext()
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context) 
    document = desktop.getCurrentComponent()   
    sheet = document.Sheets[0]
    sheet.getName()
