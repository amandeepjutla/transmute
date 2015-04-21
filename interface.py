import urwid

text = urwid.Text("menu")
fill = urwid.Filler(text, "top")
loop = urwid.MainLoop(fill)
loop.run()