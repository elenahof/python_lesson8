class Storage:
    store = []
    amount = {}

    def put(self, equip):
        if not isinstance(equip, Office):
            raise Exception("Only office equipment could be placed here")
        self.store.append(equip)
        if self.amount.get(equip.type) is not None:
            self.amount[equip.type] += 1
        else:
            self.amount.setdefault(equip.type, 1)

    def obj(self):
        for item in self.store:
            print(item)

    def total(self):
        for x, y in self.amount.items():
            print(f"{x}: {y} pieces")


class Office:
    def __init__(self, type: str, model: str, price: int, color: str):
        self.type = type
        self.model = model
        self.price = price
        self.color = color

    def __str__(self):
        return f"Model: {self.model}, price: {self.price}, color: {self.color}"


class Printer(Office):
    def __init__(self, model: str, price: int, color: str, print_type: str, cartridge: str):
        self.print_type = print_type
        self.cartridge = cartridge
        super().__init__("Pinter", model, price, color)


class Scanner(Office):
    def __init__(self, model: str, price: int, color: str, color_depth: str, dpi: int):
        self.color_depth = color_depth
        self.dpi = dpi
        super().__init__("Scanner", model, price, color)


class Xerox(Office):
    def __init__(self, model: str, price: int, color: str, print_tech: str, max_format: int):
        self.print_tech = print_tech
        self.max_format = max_format
        super().__init__("Xerox", model, price, color)


printer1 = Printer('HP T12', 5460, 'gray', 'Laser', 'HP 123 Tri-color')
printer2 = Printer('Pantum P3300DW', 25390, 'white', 'Laser', 'DS 01103402')
scanner1 = Scanner('Epson Perf V600', 8945, 'black', '48 bit', '6400x9600')
scanner2 = Scanner('Canon CanoScan', 6789, 'gray', '48 bit', '2400x2400')
xerox1 = Xerox('Canon Pixma TS3140', 2978, 'black', 'jet', '4800x1200')
xerox2 = Xerox('HP DeskJet 2630', 33829, 'white', 'jet', '1200x1200')
xerox3 = Xerox('Xerox WorkCentre 3215NI', 15487, 'black', 'laser', '4800x600')

warehouse = Storage()
warehouse.put(printer1)
warehouse.put(printer2)
warehouse.put(scanner1)
warehouse.put(scanner2)
warehouse.put(xerox1)
warehouse.put(xerox2)
warehouse.put(xerox3)

warehouse.obj()
warehouse.total()