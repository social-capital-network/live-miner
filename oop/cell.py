from chromo import Chromo


class Cell(Chromo):
    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.patrons = []

    def add_patrons(self, patrons):
        self.patrons.extend(patrons)


cell1 = Cell(150)
cell1.add_warning('Test')
cell1.add_patrons(['Linus', 'Tim', 'Mary'])
print(cell1.patrons)
cell1.run()
