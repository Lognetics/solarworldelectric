# -*- coding: utf-8 -*-
"""
Spinning dot-globe.

The map is drawn as a dot matrix on a 2x-wide strip that translates inside a
circular mask, which is the classic way to fake a rotating sphere cheaply.
Landmasses are approximated as a union of ellipses in grid space — decorative,
not cartographic.
"""

COLS, ROWS = 72, 32

# (cx, cy, rx, ry) in grid units — a rough world silhouette
LAND = [
    # North America
    (16, 5, 8.4, 3.4), (18, 8.4, 6.2, 3.0), (13.5, 10.5, 3.0, 2.0), (20.5, 11, 2.4, 1.6),
    (10, 4, 4.0, 2.0),
    # Greenland
    (31, 3, 3.2, 2.0),
    # South America
    (25, 17, 3.8, 2.6), (26.6, 21, 2.6, 3.4), (27, 25, 1.5, 2.0),
    # Europe
    (39, 6, 4.6, 2.2), (42, 8.4, 3.0, 1.6), (36, 7, 1.6, 1.2),
    # Africa
    (41, 13, 5.2, 3.0), (42.6, 18, 3.6, 4.0), (43, 22, 2.2, 1.8),
    # Middle East
    (47, 11.5, 3.0, 2.0),
    # Asia
    (55, 6, 10.5, 3.6), (60, 9.6, 7.0, 2.6), (64.5, 7, 4.0, 2.0), (48, 6, 5.0, 2.4),
    # India
    (56, 13, 2.6, 2.4),
    # SE Asia + Indonesia
    (60, 15, 3.0, 1.6), (63, 16.6, 3.6, 1.2), (65.5, 17.6, 2.0, 1.0),
    # Australia
    (66, 21, 4.2, 2.4), (68.4, 23.2, 2.0, 1.2),
    # New Zealand
    (70.5, 24.6, 0.9, 1.3),
]

# Energy nodes: (col, row, label) — Nigeria highlighted
NODES = [(41.5, 13.5, True), (16, 6, False), (39, 6, False), (57, 8, False),
         (26, 19, False), (66, 21, False), (43, 18, False)]


def _in_land(c, r):
    for cx, cy, rx, ry in LAND:
        dx = (c - cx) / rx
        dy = (r - cy) / ry
        if dx * dx + dy * dy <= 1.0:
            return True
    return False


def map_svg(width=720, height=320):
    """One tile of the map strip. Two of these sit side by side and scroll."""
    sx = width / COLS
    sy = height / ROWS
    dots = []
    for r in range(ROWS):
        for c in range(COLS):
            if _in_land(c, r):
                x = round((c + 0.5) * sx, 1)
                y = round((r + 0.5) * sy, 1)
                dots.append('<circle cx="%s" cy="%s" r="%s"/>' % (x, y, round(sx * 0.30, 2)))

    nodes = []
    for c, r, is_ng in NODES:
        x = round((c + 0.5) * sx, 1)
        y = round((r + 0.5) * sy, 1)
        if is_ng:
            nodes.append(
                '<g class="globe__node globe__node--ng">'
                '<circle cx="%s" cy="%s" r="%s" fill="#F9B000" opacity=".28">'
                '<animate attributeName="r" values="%s;%s;%s" dur="2.6s" repeatCount="indefinite"/>'
                '<animate attributeName="opacity" values=".45;0;.45" dur="2.6s" repeatCount="indefinite"/>'
                '</circle>'
                '<circle cx="%s" cy="%s" r="%s" fill="#FFC83D"/></g>'
                % (x, y, sx * 0.7, sx * 0.7, sx * 2.6, sx * 0.7, x, y, sx * 0.66))
        else:
            nodes.append(
                '<circle class="globe__node" cx="%s" cy="%s" r="%s" fill="#4FE08C" opacity=".85">'
                '<animate attributeName="opacity" values=".35;.95;.35" dur="%ss" repeatCount="indefinite"/>'
                '</circle>' % (x, y, sx * 0.42, round(2.2 + (c % 5) * 0.6, 1)))

    return ('<svg viewBox="0 0 %d %d" preserveAspectRatio="none" aria-hidden="true">'
            '<g class="globe__dots">%s</g>%s</svg>'
            % (width, height, "".join(dots), "".join(nodes)))


def globe_block(pins=None):
    """Full globe component: rotating map, sphere shading, orbit rings, pins."""
    pins = pins or [
        ("Abuja", "8%", "20%"),
        ("Lagos", "-4%", "52%"),
        ("Port Harcourt", "62%", "84%"),
    ]
    tile = map_svg()
    pin_html = "".join(
        '<span class="globe__pin" style="left:%s;top:%s;animation-delay:%.1fs"><i></i>%s</span>'
        % (left, top, i * 0.9, label)
        for i, (label, left, top) in enumerate(pins)
    )
    return """
<div class="globe-wrap" data-reveal="zoom">
  <div class="globe">
    <div class="globe__map">%s%s</div>
    <div class="globe__shine"></div>
  </div>
  <div class="globe__ring" aria-hidden="true"></div>
  <div class="globe__ring globe__ring--2" aria-hidden="true"></div>
  %s
</div>""" % (tile, tile, pin_html)
