import socket
localContext = uno.getComponentContext()

resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext )

ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )smgr = ctx.ServiceManager

desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)

model = desktop.getCurrentComponent()

text = model.Text

cursor = text.createTextCursor()

text.insertString( cursor, "Hello World", 0 )
ctx.ServiceManager
