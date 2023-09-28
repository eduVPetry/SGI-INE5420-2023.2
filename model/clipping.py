from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.window import Window


def point_clipping(x: float, y: float, _window: "Window") -> bool:
    return _window.X_MIN_NORM <= x <= _window.X_MAX_NORM and \
           _window.Y_MIN_NORM <= y <= _window.Y_MAX_NORM

INSIDE = 0b0000
LEFT = 0b0001
RIGHT = 0b0010
BOTTOM = 0b0100
TOP = 0b1000

def compute_outcode(x: float, y: float, _window: "Window") -> int:
    outcode = INSIDE
    if x < _window.X_MIN_NORM:
        outcode |= LEFT
    elif x > _window.X_MAX_NORM:
        outcode |= RIGHT
    if y < _window.Y_MIN_NORM:
        outcode |= BOTTOM
    elif y > _window.Y_MAX_NORM:
        outcode |= TOP
    return outcode

def cohen_sutherland_clipping(x0: float, y0: float, x1: float, y1: float, _window: "Window"):
    outcode0 = compute_outcode(x0, y0, _window)
    outcode1 = compute_outcode(x1, y1, _window)
    accept = False

    while True:
        if not (outcode0 | outcode1):
            # draw without clipping
            accept = True
            break

        if outcode0 & outcode1:
            break  # discard without drawing

        outcode_out = max(outcode0, outcode1)

        if outcode_out & TOP:
            x = x0 + (x1 - x0) * (_window.Y_MAX_NORM - y0) / (y1 - y0)
            y = _window.Y_MAX_NORM
        elif outcode_out & BOTTOM:
            x = x0 + (x1 - x0) * (_window.Y_MIN_NORM - y0) / (y1 - y0)
            y = _window.Y_MIN_NORM
        elif outcode_out & RIGHT:
            y = y0 + (y1 - y0) * (_window.X_MAX_NORM - x0) / (x1 - x0)
            x = _window.X_MAX_NORM
        elif outcode_out & LEFT:
            y = y0 + (y1 - y0) * (_window.X_MIN_NORM - x0) / (x1 - x0)
            x = _window.X_MIN_NORM

        if outcode_out == outcode0:
            x0, y0 = x, y
            outcode0 = compute_outcode(x0, y0, _window)
        else:
            x1, y1 = x, y
            outcode1 = compute_outcode(x1, y1, _window)

    return accept, [(x0, y0), (x1, y1)]

def liang_barsky_clipping(x0: float, y0: float, x1: float, y1: float, _window: "Window"):
    p1 = -(x1 - x0)
    p2 = -p1
    p3 = -(y1 - y0)
    p4 = -p3

    q1 = x0 - _window.X_MIN_NORM
    q2 = _window.X_MAX_NORM - x0
    q3 = y0 - _window.Y_MIN_NORM
    q4 = _window.Y_MAX_NORM - y0

    pos_arr = [1]
    neg_arr = [0]

    if (p1 == 0 and q1 < 0) or (p2 == 0 and q2 < 0) or (p3 == 0 and q3 < 0) or (p4 == 0 and q4 < 0):
        # line is parallel and completely outside the clipping boundaries
        return False, []

    if p1 != 0:
        r1 = q1 / p1
        r2 = q2 / p2
        if p1 < 0:
            neg_arr.append(r1)
            pos_arr.append(r2)
        else:
            neg_arr.append(r2)
            pos_arr.append(r1)

    if p3 != 0:
        r3 = q3 / p3
        r4 = q4 / p4
        if p3 < 0:
            neg_arr.append(r3)
            pos_arr.append(r4)
        else:
            neg_arr.append(r4)
            pos_arr.append(r3)

    rn0 = max(neg_arr)
    rn1 = min(pos_arr)

    if rn0 > rn1:
        # line is completely outside the clipping boundaries
        return False, []

    xn0 = x0 + p2 * rn0
    yn0 = y0 + p4 * rn0
    xn1 = x0 + p2 * rn1
    yn1 = y0 + p4 * rn1

    return True, [(xn0, yn0), (xn1, yn1)]
