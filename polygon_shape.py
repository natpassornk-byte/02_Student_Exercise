"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
"""Polygon class for the Object-Oriented Polygon Art exercise."""
import turtle


class Polygon:
    """A regular polygon that draws itself with its own Turtle."""

    def __init__(self, x, y, sides, side_length, color, pen_size, angle=0):
        if sides < 3:
            raise ValueError("sides must be at least 3")
        if side_length <= 0:
            raise ValueError("side_length must be positive")
        if pen_size <= 0:
            raise ValueError("pen_size must be positive")

        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen_size = pen_size
        self._angle = angle

        # Each Polygon owns one Turtle, so pen settings and clear()
        # affect only this polygon.
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)

    def draw(self):
        """Draw the polygon at its current position."""
        pen = self._pen
        pen.color(self._color)
        pen.pensize(self._pen_size)
        pen.penup()
        pen.goto(self._x, self._y)
        pen.setheading(self._angle)
        pen.pendown()
        turn_angle = 360 / self._sides  # derived, not stored
        for _ in range(self._sides):
            pen.forward(self._side_length)
            pen.left(turn_angle)
        pen.penup()

    def move_to(self, x, y):
        """Erase this polygon only, then redraw it at (x, y)."""
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()