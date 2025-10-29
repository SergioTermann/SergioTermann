from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 800, 1000

def lerp(a, b, t):
    return int(a + (b - a) * t)

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def draw_gradient_bg(img):
    top = hex_to_rgb('#0f2027')
    bottom = hex_to_rgb('#2c5364')
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        r = lerp(top[0], bottom[0], t)
        g = lerp(top[1], bottom[1], t)
        b = lerp(top[2], bottom[2], t)
        ImageDraw.Draw(img).line([(0, y), (WIDTH, y)], fill=(r, g, b))

def load_font(size):
    try:
        return ImageFont.truetype('C:/Windows/Fonts/arial.ttf', size)
    except Exception:
        return ImageFont.load_default()

def rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill, outline=outline, width=width)

def draw_timeline(img):
    draw = ImageDraw.Draw(img)

    # Grid
    for x in range(0, WIDTH, 40):
        draw.line([(x, 0), (x, HEIGHT)], fill=(255, 255, 255, 20))
    for y in range(0, HEIGHT, 40):
        draw.line([(0, y), (WIDTH, y)], fill=(255, 255, 255, 20))

    # Title
    title_font = load_font(28)
    draw.text((WIDTH//2, 52), 'Career Timeline', font=title_font, fill=(230, 237, 243), anchor='mm')

    # Timeline line
    line_x = WIDTH//2
    draw.line([(line_x, 100), (line_x, 950)], fill=(101, 145, 249), width=5)

    # Common fonts
    year_font = load_font(16)
    title_item_font = load_font(18)
    desc_font = load_font(14)

    card_fill = (11, 19, 32)
    card_outline = (45, 59, 85)
    dot_fill = (37, 117, 252)

    entries = [
        {
            'y': 150,
            'side': 'right',
            'year': '2022 – Present',
            'title': 'PhD in Automation — Beihang University (BUAA)',
            'desc': ['Focus: Reinforcement Learning & Robotics', 'Research on intelligent agents and control'],
            'badge': 'EDUCATION'
        },
        {
            'y': 300,
            'side': 'left',
            'year': '2020 – 2022',
            'title': 'Chinese Academy of Sciences — Institute of Automation',
            'desc': ['AI Competitions & Research', 'Procgen RL Challenge — Global Top 10 (NeurIPS 2020)'],
            'badge': 'RESEARCH'
        },
        {
            'y': 450,
            'side': 'right',
            'year': '2019 – 2021',
            'title': 'Master of Engineering — Beihang University (BUAA)',
            'desc': ['Software Engineering', 'Outstanding Graduate — Beijing'],
            'badge': 'EDUCATION'
        },
        {
            'y': 600,
            'side': 'left',
            'year': 'Jun – Sep 2019',
            'title': 'Beihang Software Institute',
            'desc': ['Autonomous Driving Project', 'Algorithm development & integration'],
            'badge': 'INTERNSHIP'
        },
        {
            'y': 750,
            'side': 'right',
            'year': '2014 – 2018',
            'title': 'Bachelor of Engineering — Beijing University of Technology',
            'desc': ['Measurement & Control Technology and Instruments', 'Outstanding Thesis'],
            'badge': 'EDUCATION'
        },
        {
            'y': 900,
            'side': 'left',
            'year': 'Apr – Oct 2024',
            'title': 'Aerospace Intelligence Project',
            'desc': ['Large-Scale Parallel Reinforcement Learning', 'Multi-Modal Large Model Training'],
            'badge': 'PROJECT'
        },
    ]

    for e in entries:
        cx, cy = line_x, e['y']
        # Dot
        draw.ellipse([cx-10, cy-10, cx+10, cy+10], fill=dot_fill)

        if e['side'] == 'right':
            x1, y1 = cx+20, cy-60
            x2, y2 = x1+320, y1+120
            text_x = x1+20
        else:
            x2, y2 = cx-20, cy+60
            x1, y1 = x2-320, y2-120
            text_x = x1+20

        # Card
        rounded_rect(draw, (x1, y1, x2, y2), radius=12, fill=card_fill, outline=card_outline, width=1)

        # Year
        draw.text((text_x, y1+10), e['year'], font=year_font, fill=(157, 178, 201))
        # Title
        draw.text((text_x, y1+35), e['title'], font=title_item_font, fill=(230, 237, 243))

        # Descriptions
        dy = 60
        for d in e['desc']:
            draw.text((text_x, y1+dy), d, font=desc_font, fill=(181, 195, 214))
            dy += 22

        # Badge (simple capsule)
        badge_w = max(80, 18 * len(e['badge']) // 2)
        if e['side'] == 'right':
            bx, by = x2-90, y1+10
        else:
            bx, by = x1+10, y1+10
        rounded_rect(draw, (bx, by, bx+80, by+24), radius=12, fill=(37, 117, 252))
        draw.text((bx+40, by+12), e['badge'], font=ImageFont.load_default(), fill=(255, 255, 255), anchor='mm')

def main():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw_gradient_bg(img)
    draw_timeline(img)
    img.save('images/timeline.png')

if __name__ == '__main__':
    main()