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

    @property
    def row(self):
        return self._get_entire_x(DirectionSelector.row)
    @property
    def column(self):
        return self._get_entire_x(DirectionSelector.column)
    @property
    def left_of(self):
        return self._get_entire_x(DirectionSelector.left)
    @property
    def right_of(self):
        return self._get_entire_x(DirectionSelector.right)
    @property
    def above(self):
        return self._get_entire_x(DirectionSelector.up)
    @property
    def below(self):
        return self._get_entire_x(DirectionSelector.down)

    def set_linked_node(self, node, direction: DirectionSelector):
        match direction:
            case DirectionSelector.right:
                node.left = self
            case DirectionSelector.left:
                node.right = self
            case DirectionSelector.up:
                node.down = self
            case DirectionSelector.down:
                node.up = self
            case _:
                raise ValueError("Direction must be one of right, left, up, down")

        setattr(self, direction, node)


    def _get_entire_x(self, direction: DirectionSelector):

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
                        node.set_linked_node(next_node, DirectionSelector.up)
                if row < len(data) - 1:
                    if next_node := self.return_node_or_none(row + 1, column):
                        node.set_linked_node(next_node, DirectionSelector.down)
                if column > 0:
                    if next_node := self.return_node_or_none(row, column - 1):
                        node.set_linked_node(next_node, DirectionSelector.left)
                if column < len(row_list) - 1:
                    if next_node := self.return_node_or_none(row, column + 1):
                        node.set_linked_node(next_node, DirectionSelector.right)

                self.nodes[row].append(node)

    def __getitem__(self, x):
        return self.nodes[x]

    def return_node_or_none(self, x, y):
        try:
            return self.nodes[x][y]
        except IndexError:
            return None

    def iter_nodes(self):
        for row in self.nodes:
            yield from row

    def __repr__(self) -> str:
        return f"LinkedMatrix({self.data})"
