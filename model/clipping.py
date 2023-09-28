from typing import List, Tuple


XMIN = YMIN = -1
XMAX = YMAX = 1
CENTER = (0, 0)

A = [(-4, 0.5), (-0.1, 2.5)]
B = [(-1.5, 0), (0.9, 0.4)]
C = [(-1.5, -1), (1, 0.5)]
D = [(0.4, -0.2), (2.8, 1.5)]

#############################

def point_clipping(x: float, y: float) -> bool:
    ...

INSIDE = 0b0000
LEFT = 0b0001
RIGHT = 0b0010
BOTTOM = 0b0100
TOP = 0b1000

def compute_outcode(x: float, y: float) -> int:
    outcode = INSIDE
    if x < XMIN:
        outcode |= LEFT
    elif x > XMAX:
        outcode |= RIGHT
    if y < YMIN:
        outcode |= BOTTOM
    elif y > YMAX:
        outcode |= TOP
    return outcode

def cohen_sutherland_clipping(x0: float, y0: float, x1: float, y1: float) -> List[Tuple[float, float], Tuple[float, float]]:
    outcode0 = compute_outcode(x0, y0)
    outcode1 = compute_outcode(x1, y1)

    while True:
        if not (outcode0 | outcode1):
            break  # desenha sem clipar

        if outcode0 & outcode1:
            break  # descarta sem desenhar

        outcode_out = max(outcode0, outcode1)

        if outcode_out & TOP:
            x = x0 + (x1 - x0) * (YMAX - y0) / (y1 - y0)
            y = YMAX
        elif outcode_out & BOTTOM:
            x = x0 + (x1 - x0) * (YMIN - y0) / (y1 - y0)
            y = YMIN
        elif outcode_out & RIGHT:
            y = y0 + (y1 - y0) * (XMAX - x0) / (x1 - x0)
            x = XMAX
        elif outcode_out & LEFT:
            y = y0 + (y1 - y0) * (XMIN - x0) / (x1 - x0)
            x = XMIN

        if outcode_out == outcode0:
            x0, y0 = x, y
            outcode0 = compute_outcode(x0, y0)
        else:
            x1, y1 = x, y
            outcode1 = compute_outcode(x1, y1)

    return [(x0, y0), (x1, y1)]

def liang_barsky_clipping(x0: float, y0: float, x1: float, y1: float) -> List[Tuple[float, float], Tuple[float, float]]:
    p1 = -(x1 - x0)
    p2 = -p1
    p3 = -(y1 - y0)
    p4 = -p3

    q1 = x0 - XMIN
    q2 = XMAX - x0
    q3 = y0 - YMIN
    q4 = YMAX - y0

    pos_arr = [1]
    neg_arr = [0]

    if (p1 == 0 and q1 < 0) or (p2 == 0 and q2 < 0) or (p3 == 0 and q3 < 0) or (p4 == 0 and q4 < 0):
        return "A reta é paralela à window."

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
        return "A reta está fora da window."

    xn0 = x0 + p2 * rn0
    yn0 = y0 + p4 * rn0
    xn1 = x0 + p2 * rn1
    yn1 = y0 + p4 * rn1

    return [(xn0, yn0), (xn1, yn1)]
