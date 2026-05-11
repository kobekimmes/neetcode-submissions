class CountSquares:

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] = self.points.get((point[0], point[1]), 0) + 1
        

    def count(self, point: List[int]) -> int:

        x, y = point

        sqs = 0

        for p, freq in self.points.items():
            px, py = p

            dy, dx = y - py, x - px

            if dx != 0 and abs(dy/dx) == 1:
                sqs += freq * self.points.get((x, py) , 0) * self.points.get((px, y), 0)

        return sqs

        
