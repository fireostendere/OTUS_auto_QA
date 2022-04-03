class Figure:

    def __init__(self):
        raise RuntimeError("Невозможно создать фигуру")

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError("Переданы некорректные объекты.")
