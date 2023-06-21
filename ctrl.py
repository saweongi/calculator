class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calulate(self):
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(sel, a, b):
        try:
            return str(a+b)
        except:
            return "Calculation Error"




