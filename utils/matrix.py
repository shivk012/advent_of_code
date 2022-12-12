import enum


class DirectionSelector(str, enum.Enum):
    right = "right"
    left = "left"
    up = "up"
    down = "down"
    row = "row"
    column = "column"


class FourWayNode:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def get_entire_x(self, direction: DirectionSelector):

        output = []

        match direction:
            case DirectionSelector.row:
                output.extend(
                    self._get_singular_direction(DirectionSelector.left)[::-1]
                )
                output.append(self.value)
                output.extend(self._get_singular_direction(DirectionSelector.right))
            case DirectionSelector.column:
                output.extend(self._get_singular_direction(DirectionSelector.up)[::-1])
                output.append(self.value)
                output.extend(self._get_singular_direction(DirectionSelector.down))
            case DirectionSelector.left | DirectionSelector.up:
                output.extend(self._get_singular_direction(direction)[::-1])
            case DirectionSelector.right | DirectionSelector.down:
                output.extend(self._get_singular_direction(direction))
        return output

    def _get_singular_direction(self, direction: DirectionSelector):

        output = []

        if direction not in [
            DirectionSelector.right,
            DirectionSelector.left,
            DirectionSelector.up,
            DirectionSelector.down,
        ]:
            raise ValueError("Direction must be one of right, left, up, down")

        node = getattr(self, direction)

        while node:
            output.append(node.value)
            node = getattr(node, direction)

        return output

    def __repr__(self) -> str:
        return f"FourWayNode({self.x}, {self.y}, {self.value})"


class LinkedMatrix:
    """
    Custom class to represent a 'linked' matrix of FourWayNodes.

    Makes it easier to do advent of code puzzles that have matrices as inputs
    Input is of the format of a list of lists. For example:
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    """

    def __init__(self, data: list):
        self.data = data
        self.nodes = []
        self.matrix = self._build_matrix()

    def _build_matrix(self):
        data = self.data

        for row, row_list in enumerate(data):
            self.nodes.append([])
            for column, value in enumerate(row_list):
                node = FourWayNode(row, column, value)
                if row > 0:
                    if next_node := self.return_node_or_none(row - 1, column):
                        node.up = next_node
                        next_node.down = node
                if row < len(data) - 1:
                    if next_node := self.return_node_or_none(row + 1, column):
                        node.down = next_node
                        next_node.up = node
                if column > 0:
                    if next_node := self.return_node_or_none(row, column - 1):
                        node.left = next_node
                        next_node.right = node
                if column < len(row_list) - 1:
                    if next_node := self.return_node_or_none(row, column + 1):
                        node.right = next_node
                        next_node.left = node
                self.nodes[row].append(node)

    def __getitem__(self, x):
        return self.nodes[x]

    def return_node_or_none(self, x, y):
        try:
            return self.nodes[x][y]
        except IndexError:
            return None

    def __repr__(self) -> str:
        return f"LinkedMatrix({self.data})"

