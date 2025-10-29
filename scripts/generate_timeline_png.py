from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 1600
MARGIN_TOP, MARGIN_BOTTOM = 100, 100

def lerp(a, b, t):
    return int(a + (b - a) * t)

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def draw_gradient_bg(img):
    top = hex_to_rgb('#0f2027')
    bottom = hex_to_rgb('#2c5364')
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        r = lerp(top[0], bottom[0], t)
        g = lerp(top[1], bottom[1], t)
        b = lerp(top[2], bottom[2], t)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

def load_font(size, bold=False):
    try:
        path = 'C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf'
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill, outline=outline, width=width)

def draw_text_wrapped(draw, text, font, fill, x, y, max_width, line_height):
    words = text.split(' ')
    lines = []
    line = ''
    for w in words:
        test = (line + ' ' + w).strip()
        wlen = draw.textlength(test, font=font)
        if wlen <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    for i, l in enumerate(lines):
        draw.text((x, y + i * line_height), l, font=font, fill=fill)
    return y + len(lines) * line_height, len(lines)

def draw_timeline(img):
    draw = ImageDraw.Draw(img)

    # Title
    title_font = load_font(42, bold=True)
    draw.text((WIDTH//2, 60), 'Career Timeline', font=title_font, fill=(230, 237, 243), anchor='mm')

    # Timeline line
    line_x = WIDTH//2
    draw.line([(line_x, MARGIN_TOP), (line_x, HEIGHT - MARGIN_BOTTOM)], fill=(101, 145, 249), width=8)

    # Common fonts
    year_font = load_font(22, bold=True)
    title_item_font = load_font(26, bold=True)
    desc_font = load_font(22)

    card_fill = (14, 22, 36)
    card_outline = (58, 75, 104)
    dot_fill = (37, 117, 252)

    entries = [
        {'y': 220, 'side': 'right', 'year': '2022 – Present',
         'title': 'PhD in Automation — Beihang University (BUAA)',
         'desc': ['Focus: Reinforcement Learning & Robotics', 'Research on intelligent agents and control'], 'badge': 'EDUCATION'},
        {'y': 420, 'side': 'left', 'year': '2020 – 2022',
         'title': 'Chinese Academy of Sciences — Institute of Automation',
         'desc': ['AI Competitions & Research', 'Procgen RL Challenge — Global Top 10 (NeurIPS 2020)'], 'badge': 'RESEARCH'},
        {'y': 620, 'side': 'right', 'year': '2019 – 2021',
         'title': 'Master of Engineering — Beihang University (BUAA)',
         'desc': ['Software Engineering', 'Outstanding Graduate — Beijing'], 'badge': 'EDUCATION'},
        {'y': 820, 'side': 'left', 'year': 'Jun – Sep 2019',
         'title': 'Beihang Software Institute',
         'desc': ['Autonomous Driving Project', 'Algorithm development & integration'], 'badge': 'INTERNSHIP'},
        {'y': 1020, 'side': 'right', 'year': '2014 – 2018',
         'title': 'Bachelor of Engineering — Beijing University of Technology',
         'desc': ['Measurement & Control Technology and Instruments', 'Outstanding Thesis'], 'badge': 'EDUCATION'},
        {'y': 1220, 'side': 'left', 'year': 'Apr – Oct 2024',
         'title': 'Aerospace Intelligence Project',
         'desc': ['Large-Scale Parallel Reinforcement Learning', 'Multi-Modal Large Model Training'], 'badge': 'PROJECT'},
    ]

    for e in entries:
        cx, cy = line_x, e['y']
        # Dot
        draw.ellipse([cx-12, cy-12, cx+12, cy+12], fill=dot_fill)

        # Card geometry
        card_w, card_h_min = 480, 160
        pad_x, pad_y = 24, 18
        if e['side'] == 'right':
            x1, y1 = cx + 30, cy - card_h_min // 2
            x2, y2 = x1 + card_w, y1 + card_h_min
            text_x = x1 + pad_x
        else:
            x2, y2 = cx - 30, cy + card_h_min // 2
            x1, y1 = x2 - card_w, y2 - card_h_min
            text_x = x1 + pad_x

        # Draw card base
        rounded_rect(draw, (x1, y1, x2, y2), radius=18, fill=card_fill, outline=card_outline, width=2)

        # Text content with wrapping
        current_y = y1 + pad_y
        draw.text((text_x, current_y), e['year'], font=year_font, fill=(157, 178, 201))
        current_y += 34

        current_y, title_lines = draw_text_wrapped(draw, e['title'], title_item_font, (230, 237, 243), text_x, current_y, card_w - 2 * pad_x, 30)
        current_y += 6
        for d in e['desc']:
            current_y, desc_lines = draw_text_wrapped(draw, d, desc_font, (181, 195, 214), text_x, current_y, card_w - 2 * pad_x, 28)

        # Adjust card height if content exceeded
        needed_h = max(card_h_min, (current_y - y1) + pad_y + 10)
        if needed_h > (y2 - y1):
            # redraw card with new height overlay
            rounded_rect(draw, (x1, y1, x2, y1 + needed_h), radius=18, fill=card_fill, outline=card_outline, width=2)
            # No need to redraw text; it already exists on top

        # Badge
        badge_w, badge_h = 120, 32
        if e['side'] == 'right':
            bx, by = x2 - badge_w - 16, y1 + 14
        else:
            bx, by = x1 + 16, y1 + 14
        rounded_rect(draw, (bx, by, bx + badge_w, by + badge_h), radius=16, fill=(37, 117, 252))
        draw.text((bx + badge_w // 2, by + badge_h // 2), e['badge'], font=load_font(18, bold=True), fill=(255, 255, 255), anchor='mm')

def main():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw_gradient_bg(img)
    draw_timeline(img)
    img.save('images/timeline.png')

if __name__ == '__main__':
    main()