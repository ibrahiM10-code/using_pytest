class AddToList:
    def __init__(self, lista: list, amount: int) -> None:
        self.amount = amount
        self.list = lista

    def add(self, item: int):
        self.list.append(item)
        if len(self.list) > self.amount:
            raise IndexError("Cant add more than that amount of items you provided")

    def get_list(self):
        return self.list
    
