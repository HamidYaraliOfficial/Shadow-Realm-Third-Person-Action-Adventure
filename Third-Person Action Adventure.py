import sys
import math
import random
import time
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox,
    QSlider, QDialog, QProgressDialog, QMessageBox, QFrame,
    QGridLayout, QSizePolicy, QScrollArea, QGraphicsDropShadowEffect
)
from PyQt6.QtCore import (
    Qt, QTimer, QPoint, QPointF, QRectF, QSizeF, pyqtSignal, QSize
)
from PyQt6.QtGui import (
    QPainter, QColor, QBrush, QPen, QLinearGradient, QRadialGradient,
    QFont, QFontMetrics, QPainterPath, QPolygonF, QCursor, QTransform,
    QPixmap, QIcon, QPalette, QImage
)

# ─────────────────────────── TRANSLATIONS ───────────────────────────
TR = {
    "en": {
        "title": "Shadow Realm",
        "play": "New Game",
        "continue": "Continue",
        "settings": "Settings",
        "exit": "Exit",
        "back": "Back",
        "theme": "Theme",
        "language": "Language",
        "dark": "Dark",
        "light": "Light",
        "volume": "Volume",
        "difficulty": "Difficulty",
        "easy": "Easy",
        "normal": "Normal",
        "hard": "Hard",
        "apply": "Apply",
        "cancel": "Cancel",
        "level": "Level",
        "health": "HP",
        "mana": "MP",
        "score": "Score",
        "enemies": "Enemies",
        "wave": "Wave",
        "pause": "Paused",
        "resume": "Resume",
        "main_menu": "Main Menu",
        "hero": "Hero",
        "attack": "Attack",
        "dash": "Dash",
        "spell": "Spell",
        "controls": "WASD Move • Space Attack • Shift Dash • E Spell",
        "game_over": "Game Over",
        "victory": "Victory!",
        "restart": "Restart",
        "world_select": "Select World",
        "forest": "Forest",
        "dungeon": "Dungeon",
        "castle": "Castle",
        "generating": "Loading World…",
        "new_game": "New Game",
        "kills": "Kills",
        "wave_clear": "Wave Cleared!",
        "boss": "BOSS",
    },
    "zh": {
        "title": "暗影王国",
        "play": "新游戏",
        "continue": "继续",
        "settings": "设置",
        "exit": "退出",
        "back": "返回",
        "theme": "主题",
        "language": "语言",
        "dark": "深色",
        "light": "浅色",
        "volume": "音量",
        "difficulty": "难度",
        "easy": "简单",
        "normal": "普通",
        "hard": "困难",
        "apply": "应用",
        "cancel": "取消",
        "level": "等级",
        "health": "生命",
        "mana": "法力",
        "score": "分数",
        "enemies": "敌人",
        "wave": "波次",
        "pause": "已暂停",
        "resume": "继续游戏",
        "main_menu": "主菜单",
        "hero": "英雄",
        "attack": "攻击",
        "dash": "冲刺",
        "spell": "法术",
        "controls": "WASD移动 • 空格攻击 • Shift冲刺 • E法术",
        "game_over": "游戏结束",
        "victory": "胜利！",
        "restart": "重新开始",
        "world_select": "选择世界",
        "forest": "森林",
        "dungeon": "地牢",
        "castle": "城堡",
        "generating": "加载世界…",
        "new_game": "新游戏",
        "kills": "击杀",
        "wave_clear": "波次完成！",
        "boss": "首领",
    },
    "fa": {
        "title": "قلمرو سایه",
        "play": "بازی جدید",
        "continue": "ادامه",
        "settings": "تنظیمات",
        "exit": "خروج",
        "back": "بازگشت",
        "theme": "پوسته",
        "language": "زبان",
        "dark": "تاریک",
        "light": "روشن",
        "volume": "صدا",
        "difficulty": "سختی",
        "easy": "آسان",
        "normal": "معمولی",
        "hard": "سخت",
        "apply": "اعمال",
        "cancel": "لغو",
        "level": "سطح",
        "health": "HP",
        "mana": "MP",
        "score": "امتیاز",
        "enemies": "دشمنان",
        "wave": "موج",
        "pause": "مکث",
        "resume": "ادامه",
        "main_menu": "منوی اصلی",
        "hero": "قهرمان",
        "attack": "حمله",
        "dash": "داش",
        "spell": "طلسم",
        "controls": "WASD حرکت • فاصله حمله • Shift داش • E طلسم",
        "game_over": "بازی تمام شد",
        "victory": "پیروزی!",
        "restart": "شروع مجدد",
        "world_select": "انتخاب جهان",
        "forest": "جنگل",
        "dungeon": "سیاه‌چال",
        "castle": "قلعه",
        "generating": "بارگذاری دنیا…",
        "new_game": "بازی جدید",
        "kills": "کشته",
        "wave_clear": "موج پاک شد!",
        "boss": "باس",
    },
}

# ─────────────────────────── THEMES ───────────────────────────
TH = {
    "dark": {
        "bg": "#0d0d1a",
        "bg2": "#1a1a2e",
        "bg3": "#16213e",
        "card": "#1e1e3a",
        "card2": "#252545",
        "text": "#e8e8ff",
        "text2": "#a0a0cc",
        "accent": "#7c4dff",
        "accent2": "#ff4081",
        "accent3": "#00e5ff",
        "btn": "#2d2d5e",
        "btn_hover": "#5c35cc",
        "btn_text": "#e8e8ff",
        "border": "#3d3d7a",
        "hp": "#ff4444",
        "mp": "#4488ff",
        "xp": "#44ff88",
        "gold": "#ffcc00",
        "enemy": "#ff3333",
        "hero": "#44aaff",
        "boss": "#ff6600",
        "ground": "#1a2a1a",
        "wall": "#2a1a3a",
        "particle": "#ffcc44",
        "shadow": "#000022",
        "overlay": "#00000099",
    },
    "light": {
        "bg": "#e8eaf6",
        "bg2": "#c5cae9",
        "bg3": "#dde1f4",
        "card": "#ffffff",
        "card2": "#f3f4ff",
        "text": "#1a1a3a",
        "text2": "#4a4a8a",
        "accent": "#5c35cc",
        "accent2": "#e91e63",
        "accent3": "#0097a7",
        "btn": "#ede7f6",
        "btn_hover": "#7c4dff",
        "btn_text": "#1a1a3a",
        "border": "#b0b0dd",
        "hp": "#d32f2f",
        "mp": "#1565c0",
        "xp": "#2e7d32",
        "gold": "#f57f17",
        "enemy": "#c62828",
        "hero": "#1565c0",
        "boss": "#e65100",
        "ground": "#aabbaa",
        "wall": "#998899",
        "particle": "#ff8800",
        "shadow": "#00000044",
        "overlay": "#ffffff99",
    },
}

# ─────────────────────────── GAME ENTITIES ───────────────────────────
class Vec2:
    __slots__ = ("x", "y")
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, o): return Vec2(self.x + o.x, self.y + o.y)
    def __sub__(self, o): return Vec2(self.x - o.x, self.y - o.y)
    def __mul__(self, s): return Vec2(self.x * s, self.y * s)
    def __rmul__(self, s): return self.__mul__(s)
    def length(self): return math.hypot(self.x, self.y)
    def normalized(self):
        l = self.length()
        return Vec2(self.x / l, self.y / l) if l > 1e-9 else Vec2()
    def dot(self, o): return self.x * o.x + self.y * o.y
    def copy(self): return Vec2(self.x, self.y)


class Particle:
    def __init__(self, x, y, vx, vy, life, color, size=4, ptype="circle"):
        self.pos = Vec2(x, y)
        self.vel = Vec2(vx, vy)
        self.life = life
        self.max_life = life
        self.color = color
        self.size = size
        self.ptype = ptype

    def update(self, dt):
        self.pos = self.pos + self.vel * dt
        self.vel = self.vel * (1.0 - 2.5 * dt)
        self.life -= dt
        return self.life > 0


class Projectile:
    def __init__(self, x, y, vx, vy, damage, owner, color="#ffcc44", radius=6):
        self.pos = Vec2(x, y)
        self.vel = Vec2(vx, vy)
        self.damage = damage
        self.owner = owner  # "hero" or "enemy"
        self.color = color
        self.radius = radius
        self.alive = True
        self.life = 3.0

    def update(self, dt):
        self.pos = self.pos + self.vel * dt
        self.life -= dt
        if self.life <= 0:
            self.alive = False


class Enemy:
    TYPES = {
        "grunt": {"hp": 60, "speed": 70, "damage": 12, "radius": 16, "color": "#ff4444", "xp": 20, "score": 50},
        "archer": {"hp": 40, "speed": 55, "damage": 8, "radius": 14, "color": "#ff8844", "xp": 25, "score": 60},
        "tank": {"hp": 160, "speed": 45, "damage": 20, "radius": 22, "color": "#aa2222", "xp": 40, "score": 100},
        "boss": {"hp": 600, "speed": 60, "damage": 30, "radius": 35, "color": "#ff6600", "xp": 200, "score": 500},
    }

    def __init__(self, x, y, etype="grunt"):
        info = self.TYPES[etype]
        self.pos = Vec2(x, y)
        self.vel = Vec2()
        self.hp = info["hp"]
        self.max_hp = info["hp"]
        self.speed = info["speed"]
        self.damage = info["damage"]
        self.radius = info["radius"]
        self.color = info["color"]
        self.xp = info["xp"]
        self.score = info["score"]
        self.etype = etype
        self.alive = True
        self.attack_cd = 0.0
        self.shoot_cd = 0.0
        self.anim_t = random.uniform(0, math.pi * 2)
        self.hurt_t = 0.0
        self.angle = 0.0

    def update(self, dt, hero_pos, world):
        if not self.alive:
            return
        self.anim_t += dt * 3
        self.attack_cd = max(0, self.attack_cd - dt)
        self.shoot_cd = max(0, self.shoot_cd - dt)
        self.hurt_t = max(0, self.hurt_t - dt)

        dx = hero_pos.x - self.pos.x
        dy = hero_pos.y - self.pos.y
        dist = math.hypot(dx, dy)

        if dist > 1:
            self.angle = math.atan2(dy, dx)

        if self.etype == "archer" and dist < 320:
            # archers keep distance
            if dist < 130:
                nx, ny = -dx / dist, -dy / dist
                self.vel = Vec2(nx * self.speed, ny * self.speed)
            elif dist > 180:
                nx, ny = dx / dist, dy / dist
                self.vel = Vec2(nx * self.speed * 0.7, ny * self.speed * 0.7)
            else:
                self.vel = Vec2()
        elif dist < 350:
            if dist > 1:
                nx, ny = dx / dist, dy / dist
                self.vel = Vec2(nx * self.speed, ny * self.speed)
        else:
            self.vel = Vec2()

        self.pos = self.pos + self.vel * dt

    def take_damage(self, dmg):
        self.hp -= dmg
        self.hurt_t = 0.15
        if self.hp <= 0:
            self.alive = False


class Hero:
    def __init__(self, x, y):
        self.pos = Vec2(x, y)
        self.vel = Vec2()
        self.hp = 100
        self.max_hp = 100
        self.mp = 100
        self.max_mp = 100
        self.xp = 0
        self.xp_next = 100
        self.level = 1
        self.score = 0
        self.kills = 0
        self.speed = 160.0
        self.radius = 18
        self.angle = 0.0
        self.anim_t = 0.0
        self.attack_cd = 0.0
        self.dash_cd = 0.0
        self.spell_cd = 0.0
        self.hurt_t = 0.0
        self.dash_t = 0.0
        self.dash_dir = Vec2()
        self.alive = True
        self.invuln = 0.0

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_next:
            self.xp -= self.xp_next
            self.level += 1
            self.xp_next = int(self.xp_next * 1.4)
            self.max_hp = min(200, self.max_hp + 15)
            self.hp = min(self.max_hp, self.hp + 30)
            self.max_mp = min(200, self.max_mp + 10)
            self.mp = min(self.max_mp, self.mp + 20)

    def take_damage(self, dmg):
        if self.invuln > 0 or self.dash_t > 0:
            return
        self.hp -= dmg
        self.hurt_t = 0.2
        self.invuln = 0.5
        if self.hp <= 0:
            self.hp = 0
            self.alive = False


# ─────────────────────────── WORLD ───────────────────────────
class GameWorld:
    TILE_SIZE = 48

    def __init__(self, wtype="forest", difficulty="normal"):
        self.wtype = wtype
        self.difficulty = difficulty
        self.width = 32
        self.height = 24
        self.tiles = []
        self.obstacles = []  # list of QRectF
        self.decorations = []  # (x, y, dtype, color)
        self._generate()

    def _generate(self):
        rng = random.Random(int(time.time() * 1000) % 99999)
        W, H = self.width, self.height
        T = self.TILE_SIZE

        # tile map: 0=floor, 1=wall, 2=water, 3=pit
        self.tiles = [[0] * W for _ in range(H)]

        # Border walls
        for x in range(W):
            self.tiles[0][x] = 1
            self.tiles[H - 1][x] = 1
        for y in range(H):
            self.tiles[y][0] = 1
            self.tiles[y][W - 1] = 1

        if self.wtype == "dungeon":
            # Random room + corridor layout
            for _ in range(18):
                rx = rng.randint(1, W - 6)
                ry = rng.randint(1, H - 6)
                rw = rng.randint(2, 5)
                rh = rng.randint(2, 4)
                for dy in range(rh):
                    for dx in range(rw):
                        if 0 < ry + dy < H - 1 and 0 < rx + dx < W - 1:
                            self.tiles[ry + dy][rx + dx] = 1
            # Clear center area
            for y in range(H // 2 - 3, H // 2 + 4):
                for x in range(W // 2 - 4, W // 2 + 5):
                    self.tiles[y][x] = 0
        elif self.wtype == "castle":
            # Pillar grid
            for py in range(3, H - 2, 5):
                for px in range(3, W - 2, 5):
                    for dy in range(2):
                        for dx in range(2):
                            if 0 < py + dy < H - 1 and 0 < px + dx < W - 1:
                                self.tiles[py + dy][px + dx] = 1
            for y in range(H // 2 - 2, H // 2 + 3):
                for x in range(W // 2 - 3, W // 2 + 4):
                    self.tiles[y][x] = 0
        else:  # forest
            # Scattered trees/rocks
            for _ in range(25):
                tx = rng.randint(2, W - 3)
                ty = rng.randint(2, H - 3)
                dist_center = math.hypot(tx - W // 2, ty - H // 2)
                if dist_center > 5:
                    self.tiles[ty][tx] = 1

        # Build obstacle rects
        self.obstacles.clear()
        for y in range(H):
            for x in range(W):
                if self.tiles[y][x] == 1:
                    self.obstacles.append(
                        QRectF(x * T, y * T, T, T)
                    )

        # Decorations
        self.decorations.clear()
        colors = {
            "forest": ["#226622", "#228822", "#448844", "#336633"],
            "dungeon": ["#443355", "#554466", "#332244", "#663377"],
            "castle": ["#887766", "#998877", "#776655", "#aaaaaa"],
        }
        dcols = colors.get(self.wtype, colors["forest"])
        for _ in range(40):
            dx = rng.randint(1, W - 2) * T + rng.randint(0, T - 1)
            dy = rng.randint(1, H - 2) * T + rng.randint(0, T - 1)
            tx = int(dx // T)
            ty = int(dy // T)
            if self.tiles[ty][tx] == 0:
                self.decorations.append((dx, dy, rng.choice(["dot", "cross", "circle"]), rng.choice(dcols)))

    def is_wall(self, x, y):
        T = self.TILE_SIZE
        tx = int(x // T)
        ty = int(y // T)
        if tx < 0 or ty < 0 or tx >= self.width or ty >= self.height:
            return True
        return self.tiles[ty][tx] == 1

    def world_width(self):
        return self.width * self.TILE_SIZE

    def world_height(self):
        return self.height * self.TILE_SIZE


# ─────────────────────────── WAVE MANAGER ───────────────────────────
class WaveManager:
    def __init__(self, difficulty="normal"):
        self.wave = 0
        self.difficulty = difficulty
        self.enemies_remaining = 0
        self.spawn_queue = []
        self.spawn_timer = 0.0
        self.between_wave_t = 0.0
        self.active = False
        self.wave_clear_t = 0.0
        self.all_done = False
        self.max_waves = 5

    def start(self):
        self.wave = 0
        self.all_done = False
        self._next_wave()

    def _next_wave(self):
        if self.wave >= self.max_waves:
            self.all_done = True
            self.active = False
            return
        self.wave += 1
        self.spawn_queue = self._build_wave(self.wave)
        self.enemies_remaining = len(self.spawn_queue)
        self.spawn_timer = 0.0
        self.active = True
        self.wave_clear_t = 0.0

    def _build_wave(self, w):
        queue = []
        diff_mult = {"easy": 0.7, "normal": 1.0, "hard": 1.5}.get(self.difficulty, 1.0)
        n_grunt = int((2 + w * 2) * diff_mult)
        n_archer = int((w - 1) * diff_mult) if w > 1 else 0
        n_tank = int((w // 2) * diff_mult)
        has_boss = (w == self.max_waves)

        queue += ["grunt"] * n_grunt
        queue += ["archer"] * n_archer
        queue += ["tank"] * n_tank
        if has_boss:
            queue += ["boss"]
        random.shuffle(queue)
        return queue

    def update(self, dt, enemies, hero, world):
        self.wave_clear_t = max(0, self.wave_clear_t - dt)
        if not self.active:
            return [], False

        self.spawn_timer -= dt
        new_enemies = []
        if self.spawn_queue and self.spawn_timer <= 0:
            etype = self.spawn_queue.pop(0)
            spawn_pos = self._pick_spawn(hero, world)
            e = Enemy(spawn_pos.x, spawn_pos.y, etype)
            new_enemies.append(e)
            self.spawn_timer = 0.8 + random.uniform(0, 0.6)

        alive_count = sum(1 for e in enemies if e.alive)
        if not self.spawn_queue and alive_count == 0 and self.enemies_remaining > 0:
            self.wave_clear_t = 2.5
            self.enemies_remaining = 0
            self.active = False
            self.between_wave_t = 3.0
            return new_enemies, True

        if not self.active and self.between_wave_t > 0:
            self.between_wave_t -= dt
            if self.between_wave_t <= 0:
                self._next_wave()

        return new_enemies, False

    def _pick_spawn(self, hero, world):
        T = world.TILE_SIZE
        for _ in range(40):
            margin = 4
            x = random.randint(margin, world.width - margin - 1) * T + T // 2
            y = random.randint(margin, world.height - margin - 1) * T + T // 2
            dist = math.hypot(x - hero.pos.x, y - hero.pos.y)
            if dist > 220 and not world.is_wall(x, y):
                return Vec2(x, y)
        return Vec2(
            random.randint(1, world.width - 2) * T,
            random.randint(1, world.height - 2) * T
        )


# ─────────────────────────── GAME RENDERER ───────────────────────────
class GameRenderer(QWidget):
    request_menu = pyqtSignal()
    request_restart = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self.lang = "en"
        self.world = None
        self.hero = None
        self.enemies = []
        self.projectiles = []
        self.particles = []
        self.wave_mgr = None
        self.paused = False
        self.game_over = False
        self.victory = False
        self.keys = set()
        self.mouse_pos = QPointF(0, 0)
        self.cam = Vec2()
        self.last_time = time.perf_counter()
        self.flash_msgs = []  # (msg, t_remaining, color)
        self.combo = 0
        self.combo_t = 0.0
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setMouseTracking(True)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(16)

    def t(self, k): return TR[self.lang].get(k, k)
    def tc(self): return TH[self.theme]

    def start_game(self, wtype="forest", difficulty="normal"):
        self.world = GameWorld(wtype, difficulty)
        WW = self.world.world_width()
        WH = self.world.world_height()
        cx = WW // 2
        cy = WH // 2
        self.hero = Hero(cx, cy)
        self.enemies = []
        self.projectiles = []
        self.particles = []
        self.wave_mgr = WaveManager(difficulty)
        self.wave_mgr.start()
        self.paused = False
        self.game_over = False
        self.victory = False
        self.flash_msgs = []
        self.combo = 0
        self.combo_t = 0.0
        self.last_time = time.perf_counter()
        self.setFocus()

    def _tick(self):
        if self.world is None or self.paused or self.game_over or self.victory:
            self.update()
            return

        now = time.perf_counter()
        dt = min(now - self.last_time, 0.05)
        self.last_time = now

        self._update_hero(dt)
        self._update_enemies(dt)
        self._update_projectiles(dt)
        self._update_particles(dt)
        self._update_wave(dt)
        self._update_camera()
        self._regen(dt)
        self.update()

    def _update_hero(self, dt):
        h = self.hero
        if not h.alive:
            self.game_over = True
            return

        h.anim_t += dt * 5
        h.attack_cd = max(0, h.attack_cd - dt)
        h.dash_cd = max(0, h.dash_cd - dt)
        h.spell_cd = max(0, h.spell_cd - dt)
        h.hurt_t = max(0, h.hurt_t - dt)
        h.invuln = max(0, h.invuln - dt)
        self.combo_t = max(0, self.combo_t - dt)
        if self.combo_t <= 0:
            self.combo = 0

        self.flash_msgs = [(m, t - dt, c) for m, t, c in self.flash_msgs if t - dt > 0]

        # Movement
        move = Vec2()
        spd = h.speed
        if Qt.Key.Key_W in self.keys or Qt.Key.Key_Up in self.keys:
            move.y -= 1
        if Qt.Key.Key_S in self.keys or Qt.Key.Key_Down in self.keys:
            move.y += 1
        if Qt.Key.Key_A in self.keys or Qt.Key.Key_Left in self.keys:
            move.x -= 1
        if Qt.Key.Key_D in self.keys or Qt.Key.Key_Right in self.keys:
            move.x += 1

        if h.dash_t > 0:
            h.dash_t -= dt
            move = h.dash_dir * 1.0
            spd = h.speed * 3.2
            for _ in range(3):
                angle = random.uniform(0, math.pi * 2)
                self.particles.append(Particle(
                    h.pos.x, h.pos.y,
                    math.cos(angle) * 60, math.sin(angle) * 60,
                    0.3, self.tc()["accent3"], 5
                ))
        elif move.length() > 0.1:
            move = move.normalized()
            h.angle = math.atan2(move.y, move.x)

        new_pos = Vec2(
            h.pos.x + move.x * spd * dt,
            h.pos.y + move.y * spd * dt
        )

        # Collision
        r = h.radius * 0.85
        if not self.world.is_wall(new_pos.x - r, new_pos.y) and \
           not self.world.is_wall(new_pos.x + r, new_pos.y):
            h.pos.x = new_pos.x
        if not self.world.is_wall(h.pos.x, new_pos.y - r) and \
           not self.world.is_wall(h.pos.x, new_pos.y + r):
            h.pos.y = new_pos.y

        # Clamp
        WW = self.world.world_width()
        WH = self.world.world_height()
        h.pos.x = max(h.radius, min(WW - h.radius, h.pos.x))
        h.pos.y = max(h.radius, min(WH - h.radius, h.pos.y))

        # Face mouse
        cx, cy = self._world_to_screen(h.pos.x, h.pos.y)
        mx, my = self.mouse_pos.x(), self.mouse_pos.y()
        h.angle = math.atan2(my - cy, mx - cx)

    def _attack(self):
        h = self.hero
        if h.attack_cd > 0 or not h.alive:
            return
        h.attack_cd = 0.35
        angle = h.angle
        speed = 380.0
        p = Projectile(
            h.pos.x + math.cos(angle) * 28,
            h.pos.y + math.sin(angle) * 28,
            math.cos(angle) * speed,
            math.sin(angle) * speed,
            15 + h.level * 3,
            "hero",
            self.tc()["accent3"],
            7
        )
        self.projectiles.append(p)
        for _ in range(5):
            a = angle + random.uniform(-0.4, 0.4)
            self.particles.append(Particle(
                h.pos.x + math.cos(angle) * 25,
                h.pos.y + math.sin(angle) * 25,
                math.cos(a) * 120, math.sin(a) * 120,
                0.25, self.tc()["accent3"], 4
            ))

    def _dash(self):
        h = self.hero
        if h.dash_cd > 0 or not h.alive:
            return
        h.dash_cd = 1.8
        h.dash_t = 0.18
        cx, cy = self._world_to_screen(h.pos.x, h.pos.y)
        mx, my = self.mouse_pos.x(), self.mouse_pos.y()
        dx, dy = mx - cx, my - cy
        dist = math.hypot(dx, dy)
        if dist < 1:
            dx, dy = math.cos(h.angle), math.sin(h.angle)
        else:
            dx, dy = dx / dist, dy / dist
        h.dash_dir = Vec2(dx, dy)
        self.flash_msgs.append((self.t("dash"), 0.7, self.tc()["accent3"]))

    def _spell(self):
        h = self.hero
        if h.spell_cd > 0 or h.mp < 30 or not h.alive:
            return
        h.spell_cd = 2.5
        h.mp -= 30
        angle = h.angle
        for i in range(6):
            a = angle + i * math.pi / 3
            speed = 260.0
            p = Projectile(
                h.pos.x, h.pos.y,
                math.cos(a) * speed, math.sin(a) * speed,
                22 + h.level * 4, "hero",
                self.tc()["accent2"], 9
            )
            self.projectiles.append(p)
        for _ in range(20):
            a = random.uniform(0, math.pi * 2)
            self.particles.append(Particle(
                h.pos.x, h.pos.y,
                math.cos(a) * 200, math.sin(a) * 200,
                0.6, self.tc()["accent2"], 6
            ))
        self.flash_msgs.append((self.t("spell"), 0.9, self.tc()["accent2"]))

    def _update_enemies(self, dt):
        projs_to_remove = set()
        for e in self.enemies:
            if not e.alive:
                continue
            e.update(dt, self.hero.pos, self.world)

            # Enemy collision with hero
            dist = (e.pos - self.hero.pos).length()
            if dist < e.radius + self.hero.radius:
                if e.attack_cd <= 0:
                    self.hero.take_damage(e.damage)
                    e.attack_cd = 1.2
                    for _ in range(8):
                        a = random.uniform(0, math.pi * 2)
                        self.particles.append(Particle(
                            self.hero.pos.x, self.hero.pos.y,
                            math.cos(a) * 100, math.sin(a) * 100,
                            0.4, self.tc()["hp"], 5
                        ))

            # Archer shoot
            if e.etype == "archer" and e.shoot_cd <= 0:
                hdist = (self.hero.pos - e.pos).length()
                if 80 < hdist < 310:
                    dx = self.hero.pos.x - e.pos.x
                    dy = self.hero.pos.y - e.pos.y
                    ang = math.atan2(dy, dx)
                    ep = Projectile(
                        e.pos.x + math.cos(ang) * 20,
                        e.pos.y + math.sin(ang) * 20,
                        math.cos(ang) * 220, math.sin(ang) * 220,
                        e.damage, "enemy",
                        self.tc()["enemy"], 6
                    )
                    self.projectiles.append(ep)
                    e.shoot_cd = 1.8

            # Boss special
            if e.etype == "boss" and e.shoot_cd <= 0:
                for i in range(8):
                    a = e.anim_t / 2 + i * math.pi / 4
                    bp = Projectile(
                        e.pos.x, e.pos.y,
                        math.cos(a) * 180, math.sin(a) * 180,
                        e.damage // 2, "enemy",
                        self.tc()["boss"], 8
                    )
                    self.projectiles.append(bp)
                e.shoot_cd = 2.0

        self.enemies = [e for e in self.enemies if e.alive]

    def _update_projectiles(self, dt):
        for p in self.projectiles:
            if not p.alive:
                continue
            p.update(dt)
            # Wall collision
            if self.world.is_wall(p.pos.x, p.pos.y):
                p.alive = False
                for _ in range(4):
                    a = random.uniform(0, math.pi * 2)
                    self.particles.append(Particle(
                        p.pos.x, p.pos.y,
                        math.cos(a) * 60, math.sin(a) * 60,
                        0.3, p.color, 3
                    ))
                continue

            if p.owner == "hero":
                for e in self.enemies:
                    if not e.alive:
                        continue
                    d = (e.pos - p.pos).length()
                    if d < e.radius + p.radius:
                        e.take_damage(p.damage)
                        p.alive = False
                        self.combo += 1
                        self.combo_t = 2.0
                        if not e.alive:
                            self.hero.gain_xp(e.xp)
                            self.hero.score += e.score * (1 + self.combo // 5)
                            self.hero.kills += 1
                            # Death particles
                            for _ in range(14):
                                a = random.uniform(0, math.pi * 2)
                                spd = random.uniform(60, 180)
                                self.particles.append(Particle(
                                    e.pos.x, e.pos.y,
                                    math.cos(a) * spd, math.sin(a) * spd,
                                    0.8, e.color, random.randint(4, 9)
                                ))
                            self.flash_msgs.append((f"+{e.score}", 0.8, self.tc()["gold"]))
                        break
            elif p.owner == "enemy":
                d = (self.hero.pos - p.pos).length()
                if d < self.hero.radius + p.radius:
                    self.hero.take_damage(p.damage)
                    p.alive = False

        self.projectiles = [p for p in self.projectiles if p.alive]

    def _update_particles(self, dt):
        self.particles = [p for p in self.particles if p.update(dt)]

    def _update_wave(self, dt):
        if self.wave_mgr is None:
            return
        new_enemies, wave_cleared = self.wave_mgr.update(dt, self.enemies, self.hero, self.world)
        self.enemies.extend(new_enemies)
        if wave_cleared:
            self.flash_msgs.append((self.t("wave_clear"), 2.0, self.tc()["gold"]))
        if self.wave_mgr.all_done and len(self.enemies) == 0:
            self.victory = True

    def _regen(self, dt):
        h = self.hero
        h.mp = min(h.max_mp, h.mp + 8 * dt)

    def _update_camera(self):
        if self.hero is None:
            return
        W, H = self.width(), self.height()
        target_x = self.hero.pos.x - W / 2
        target_y = self.hero.pos.y - H / 2
        WW = self.world.world_width()
        WH = self.world.world_height()
        target_x = max(0, min(WW - W, target_x))
        target_y = max(0, min(WH - H, target_y))
        # Smooth camera
        self.cam.x += (target_x - self.cam.x) * 0.12
        self.cam.y += (target_y - self.cam.y) * 0.12

    def _world_to_screen(self, wx, wy):
        return wx - self.cam.x, wy - self.cam.y

    # ── RENDERING ──
    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        p.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        W, H = self.width(), self.height()
        tc = self.tc()

        if self.world is None:
            p.fillRect(0, 0, W, H, QColor(tc["bg"]))
            p.end()
            return

        self._draw_world(p, W, H, tc)
        self._draw_decorations(p, tc)
        self._draw_particles(p, tc)
        self._draw_enemies(p, tc)
        self._draw_projectiles(p, tc)
        if self.hero and self.hero.alive:
            self._draw_hero(p, tc)
        self._draw_hud(p, W, H, tc)

        if self.paused:
            self._draw_pause(p, W, H, tc)
        if self.game_over:
            self._draw_game_over(p, W, H, tc)
        if self.victory:
            self._draw_victory(p, W, H, tc)

        p.end()

    def _draw_world(self, p, W, H, tc):
        world = self.world
        T = world.TILE_SIZE
        sx, sy = int(self.cam.x // T), int(self.cam.y // T)
        ex = min(world.width, sx + W // T + 2)
        ey = min(world.height, sy + H // T + 2)

        floor_colors = {
            "forest": ["#2d4a2d", "#2a442a", "#264024", "#304e30"],
            "dungeon": ["#1a1225", "#1e1528", "#221830", "#181020"],
            "castle": ["#3a3535", "#3e3838", "#363030", "#424040"],
        }
        wall_colors = {
            "forest": ["#1a3a1a", "#153015"],
            "dungeon": ["#2a1a40", "#22154a"],
            "castle": ["#4a3a3a", "#554545"],
        }
        fc = floor_colors.get(world.wtype, floor_colors["forest"])
        wc = wall_colors.get(world.wtype, wall_colors["forest"])

        for ty in range(max(0, sy), ey):
            for tx in range(max(0, sx), ex):
                tile = world.tiles[ty][tx]
                rx = tx * T - self.cam.x
                ry = ty * T - self.cam.y
                col_idx = (tx + ty) % len(fc)
                if tile == 1:
                    base_col = wc[col_idx % len(wc)]
                    p.fillRect(int(rx), int(ry), T + 1, T + 1, QColor(base_col))
                    # Top highlight for 3D feel
                    pen = QPen(QColor(255, 255, 255, 25))
                    pen.setWidth(1)
                    p.setPen(pen)
                    p.drawLine(int(rx), int(ry), int(rx) + T, int(ry))
                    p.drawLine(int(rx), int(ry), int(rx), int(ry) + T)
                    # Shadow edge
                    pen2 = QPen(QColor(0, 0, 0, 60))
                    p.setPen(pen2)
                    p.drawLine(int(rx) + T, int(ry), int(rx) + T, int(ry) + T)
                    p.drawLine(int(rx), int(ry) + T, int(rx) + T, int(ry) + T)
                else:
                    p.fillRect(int(rx), int(ry), T + 1, T + 1, QColor(fc[col_idx]))
                    # Subtle grid lines
                    pen = QPen(QColor(0, 0, 0, 18))
                    pen.setWidth(1)
                    p.setPen(pen)
                    p.drawRect(int(rx), int(ry), T, T)

    def _draw_decorations(self, p, tc):
        p.save()
        for dx, dy, dtype, color in self.world.decorations:
            sx, sy = self._world_to_screen(dx, dy)
            if -20 < sx < self.width() + 20 and -20 < sy < self.height() + 20:
                p.setPen(Qt.PenStyle.NoPen)
                p.setBrush(QBrush(QColor(color)))
                if dtype == "circle":
                    p.drawEllipse(QPointF(sx, sy), 5, 5)
                elif dtype == "cross":
                    pen = QPen(QColor(color), 2)
                    p.setPen(pen)
                    p.drawLine(int(sx - 4), int(sy), int(sx + 4), int(sy))
                    p.drawLine(int(sx), int(sy - 4), int(sx), int(sy + 4))
                    p.setPen(Qt.PenStyle.NoPen)
                else:
                    p.drawEllipse(QPointF(sx, sy), 3, 3)
        p.restore()

    def _draw_particles(self, p, tc):
        p.save()
        for particle in self.particles:
            sx, sy = self._world_to_screen(particle.pos.x, particle.pos.y)
            alpha = int(255 * (particle.life / particle.max_life))
            col = QColor(particle.color)
            col.setAlpha(alpha)
            p.setBrush(QBrush(col))
            p.setPen(Qt.PenStyle.NoPen)
            s = particle.size * (particle.life / particle.max_life)
            p.drawEllipse(QPointF(sx, sy), s, s)
        p.restore()

    def _draw_enemies(self, p, tc):
        p.save()
        for e in self.enemies:
            if not e.alive:
                continue
            sx, sy = self._world_to_screen(e.pos.x, e.pos.y)
            if -60 < sx < self.width() + 60 and -60 < sy < self.height() + 60:
                self._draw_enemy_sprite(p, e, sx, sy, tc)
        p.restore()

    def _draw_enemy_sprite(self, p, e, sx, sy, tc):
        r = e.radius
        bob = math.sin(e.anim_t) * 2.0
        sy += bob

        # Shadow
        p.setPen(Qt.PenStyle.NoPen)
        shadow_col = QColor(0, 0, 0, 60)
        p.setBrush(QBrush(shadow_col))
        p.drawEllipse(QPointF(sx, sy + r * 0.8), r * 0.9, r * 0.3)

        col = QColor(e.color)
        if e.hurt_t > 0:
            col = QColor("#ffffff")

        p.save()
        p.translate(sx, sy)
        p.rotate(math.degrees(e.angle))

        # Body
        grad = QRadialGradient(QPointF(-r * 0.3, -r * 0.3), r * 1.4)
        grad.setColorAt(0, col.lighter(130))
        grad.setColorAt(1, col.darker(150))
        p.setBrush(QBrush(grad))
        p.setPen(QPen(col.darker(180), 1.5))
        p.drawEllipse(QPointF(0, 0), r, r)

        # Direction indicator (face)
        p.setBrush(QBrush(QColor(255, 255, 255, 200)))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QPointF(r * 0.45, -r * 0.2), r * 0.18, r * 0.18)
        p.drawEllipse(QPointF(r * 0.45, r * 0.2), r * 0.18, r * 0.18)

        # Boss crown
        if e.etype == "boss":
            p.setPen(QPen(QColor(tc["gold"]), 2))
            p.setBrush(QBrush(QColor(tc["gold"])))
            pts = [QPointF(-r * 0.4, -r * 0.9),
                   QPointF(-r * 0.2, -r * 1.3),
                   QPointF(0, -r * 0.9),
                   QPointF(r * 0.2, -r * 1.3),
                   QPointF(r * 0.4, -r * 0.9)]
            path = QPainterPath()
            path.moveTo(pts[0])
            for pt in pts[1:]:
                path.lineTo(pt)
            path.closeSubpath()
            p.drawPath(path)

        p.restore()

        # HP bar
        bar_w = r * 2.2
        bar_h = 5
        bx = sx - bar_w / 2
        by = sy - r - 14
        hp_frac = e.hp / e.max_hp
        p.setBrush(QBrush(QColor(40, 10, 10)))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRoundedRect(QRectF(bx, by, bar_w, bar_h), 2, 2)
        hp_col = QColor("#44ff44") if hp_frac > 0.5 else QColor("#ffaa00") if hp_frac > 0.25 else QColor("#ff3333")
        p.setBrush(QBrush(hp_col))
        p.drawRoundedRect(QRectF(bx, by, bar_w * hp_frac, bar_h), 2, 2)

    def _draw_projectiles(self, p, tc):
        p.save()
        for proj in self.projectiles:
            if not proj.alive:
                continue
            sx, sy = self._world_to_screen(proj.pos.x, proj.pos.y)
            col = QColor(proj.color)
            glow_col = QColor(col)
            glow_col.setAlpha(60)
            p.setBrush(QBrush(glow_col))
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(QPointF(sx, sy), proj.radius * 1.8, proj.radius * 1.8)

            p.setBrush(QBrush(col))
            p.setPen(QPen(col.lighter(130), 1))
            p.drawEllipse(QPointF(sx, sy), proj.radius, proj.radius)

            p.setBrush(QBrush(QColor(255, 255, 255, 180)))
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(QPointF(sx - proj.radius * 0.3, sy - proj.radius * 0.3),
                          proj.radius * 0.35, proj.radius * 0.35)
        p.restore()

    def _draw_hero(self, p, tc):
        h = self.hero
        sx, sy = self._world_to_screen(h.pos.x, h.pos.y)
        r = h.radius
        bob = math.sin(h.anim_t * 0.8) * 2.5

        # Shadow
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QBrush(QColor(0, 0, 0, 70)))
        p.drawEllipse(QPointF(sx, sy + r * 0.9 + bob), r * 0.9, r * 0.28)

        p.save()
        p.translate(sx, sy + bob)

        # Invuln flash
        if h.invuln > 0 and int(h.invuln * 10) % 2 == 0:
            p.setOpacity(0.4)

        p.rotate(math.degrees(h.angle))

        # Cloak / body
        base_col = QColor(tc["hero"])
        if h.hurt_t > 0:
            base_col = QColor("#ffffff")

        grad = QRadialGradient(QPointF(-r * 0.25, -r * 0.25), r * 1.5)
        grad.setColorAt(0, base_col.lighter(140))
        grad.setColorAt(1, base_col.darker(160))
        p.setBrush(QBrush(grad))
        p.setPen(QPen(base_col.darker(200), 2))
        p.drawEllipse(QPointF(0, 0), r, r)

        # Armor details
        p.setBrush(QBrush(QColor(255, 255, 255, 80)))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(QPointF(0, 0), r * 0.55, r * 0.55)

        # Eyes
        p.setBrush(QBrush(QColor(tc["accent3"])))
        p.drawEllipse(QPointF(r * 0.4, -r * 0.25), r * 0.16, r * 0.16)
        p.drawEllipse(QPointF(r * 0.4, r * 0.25), r * 0.16, r * 0.16)

        # Weapon tip
        p.setBrush(QBrush(QColor(tc["accent"])))
        p.setPen(QPen(QColor(tc["accent"]).lighter(130), 1.5))
        path = QPainterPath()
        path.moveTo(r * 0.85, 0)
        path.lineTo(r * 1.5, -r * 0.18)
        path.lineTo(r * 1.9, 0)
        path.lineTo(r * 1.5, r * 0.18)
        path.closeSubpath()
        p.drawPath(path)

        p.restore()

        # Dash trail
        if h.dash_t > 0:
            trail_col = QColor(tc["accent3"])
            trail_col.setAlpha(100)
            p.setBrush(QBrush(trail_col))
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(QPointF(sx, sy + bob), r * 1.6, r * 1.6)

    def _draw_hud(self, p, W, H, tc):
        if self.hero is None:
            return
        h = self.hero
        scale = min(W, H) / 800.0
        scale = max(0.6, min(1.5, scale))
        pad = int(16 * scale)

        # ── Bars ──
        bar_w = int(180 * scale)
        bar_h = int(14 * scale)
        bar_x = pad
        bar_y = H - pad - bar_h * 3 - int(8 * scale)

        self._draw_bar(p, bar_x, bar_y, bar_w, bar_h,
                       h.hp / h.max_hp, tc["hp"], "HP", tc, scale)
        self._draw_bar(p, bar_x, bar_y + bar_h + int(5 * scale), bar_w, bar_h,
                       h.mp / h.max_mp, tc["mp"], "MP", tc, scale)
        xp_frac = h.xp / h.xp_next if h.xp_next > 0 else 0
        self._draw_bar(p, bar_x, bar_y + (bar_h + int(5 * scale)) * 2, bar_w, bar_h,
                       xp_frac, tc["xp"], f"Lv{h.level}", tc, scale)

        # ── Score / Wave / Kills ──
        info_x = W - pad - int(160 * scale)
        info_y = pad + int(10 * scale)
        font_sz = max(10, int(13 * scale))
        p.setFont(QFont("Arial", font_sz, QFont.Weight.Bold))

        def draw_badge(label, value, y):
            badge_w = int(155 * scale)
            badge_h = int(26 * scale)
            bg = QColor(tc["card"])
            bg.setAlpha(180)
            p.setBrush(QBrush(bg))
            p.setPen(QPen(QColor(tc["border"]), 1))
            p.drawRoundedRect(QRectF(info_x, y, badge_w, badge_h), 6, 6)
            p.setPen(QPen(QColor(tc["text2"])))
            p.drawText(QRectF(info_x + 8, y, int(badge_w * 0.45), badge_h),
                       Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, label)
            p.setPen(QPen(QColor(tc["gold"])))
            p.drawText(QRectF(info_x + int(badge_w * 0.45), y, int(badge_w * 0.5), badge_h),
                       Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter, str(value))

        wm = self.wave_mgr
        draw_badge(self.t("wave"), f"{wm.wave}/{wm.max_waves}" if wm else "0/0", info_y)
        draw_badge(self.t("score"), h.score, info_y + int(32 * scale))
        draw_badge(self.t("kills"), h.kills, info_y + int(64 * scale))

        # ── Cooldown indicators ──
        cd_y = H - pad - int(48 * scale)
        cd_x = W // 2 - int(80 * scale)
        icons = [
            (self.t("attack"), h.attack_cd, 0.35, tc["accent3"]),
            (self.t("dash"), h.dash_cd, 1.8, tc["accent3"]),
            (self.t("spell"), h.spell_cd, 2.5, tc["accent2"]),
        ]
        icon_size = int(38 * scale)
        spacing = int(50 * scale)
        p.setFont(QFont("Arial", max(8, int(9 * scale))))
        for i, (name, cd, max_cd, col) in enumerate(icons):
            ix = cd_x + i * spacing
            ready = cd <= 0
            bg = QColor(tc["card"])
            bg.setAlpha(200)
            p.setBrush(QBrush(bg))
            border_col = QColor(col) if ready else QColor(tc["border"])
            p.setPen(QPen(border_col, 1.5))
            p.drawRoundedRect(QRectF(ix, cd_y, icon_size, icon_size), 7, 7)
            if not ready:
                frac = cd / max_cd
                overlay = QColor(0, 0, 0, 140)
                p.setBrush(QBrush(overlay))
                p.setPen(Qt.PenStyle.NoPen)
                p.drawRoundedRect(
                    QRectF(ix, cd_y + icon_size * (1 - frac), icon_size, icon_size * frac), 7, 7
                )
            p.setPen(QPen(QColor(col) if ready else QColor(tc["text2"])))
            p.drawText(QRectF(ix, cd_y, icon_size, icon_size),
                       Qt.AlignmentFlag.AlignCenter, name[:3])

        # ── Combo ──
        if self.combo >= 3:
            font_sz2 = max(14, int(22 * scale))
            p.setFont(QFont("Arial", font_sz2, QFont.Weight.Bold))
            combo_col = QColor(tc["gold"])
            alpha = min(255, int(255 * (self.combo_t / 2.0)))
            combo_col.setAlpha(alpha)
            p.setPen(QPen(combo_col))
            p.drawText(
                QRectF(W // 2 - 100, H // 2 - int(80 * scale), 200, 40),
                Qt.AlignmentFlag.AlignCenter,
                f"x{self.combo} COMBO!"
            )

        # ── Flash messages ──
        fm_y = H // 2 - int(40 * scale)
        p.setFont(QFont("Arial", max(12, int(16 * scale)), QFont.Weight.Bold))
        for msg, t_rem, col_str in sorted(self.flash_msgs, key=lambda x: -x[1]):
            alpha = min(255, int(255 * t_rem))
            fc = QColor(col_str)
            fc.setAlpha(alpha)
            p.setPen(QPen(fc))
            p.drawText(QRectF(W // 2 - 120, fm_y, 240, 34),
                       Qt.AlignmentFlag.AlignCenter, msg)
            fm_y -= int(36 * scale)

        # ── Controls hint ──
        p.setFont(QFont("Arial", max(7, int(10 * scale))))
        hint_col = QColor(tc["text2"])
        hint_col.setAlpha(140)
        p.setPen(QPen(hint_col))
        p.drawText(QRectF(pad, H - pad - int(12 * scale), W - pad * 2, int(14 * scale)),
                   Qt.AlignmentFlag.AlignCenter, self.t("controls"))

        # ── Wave clear banner ──
        if wm and wm.wave_clear_t > 0:
            banner_alpha = min(255, int(255 * wm.wave_clear_t))
            p.setFont(QFont("Arial", max(18, int(26 * scale)), QFont.Weight.Bold))
            bc = QColor(tc["gold"])
            bc.setAlpha(banner_alpha)
            p.setPen(QPen(bc))
            p.drawText(QRectF(0, H // 2 - int(60 * scale), W, 50),
                       Qt.AlignmentFlag.AlignCenter,
                       f"{self.t('wave')} {wm.wave} — {self.t('wave_clear')}")

    def _draw_bar(self, p, x, y, w, h, frac, col_str, label, tc, scale):
        frac = max(0.0, min(1.0, frac))
        bg = QColor(30, 10, 10, 180)
        p.setBrush(QBrush(bg))
        p.setPen(QPen(QColor(tc["border"]), 1))
        p.drawRoundedRect(QRectF(x, y, w, h), h // 2, h // 2)

        if frac > 0:
            col = QColor(col_str)
            grad = QLinearGradient(x, y, x + w, y)
            grad.setColorAt(0, col.lighter(110))
            grad.setColorAt(1, col.darker(120))
            p.setBrush(QBrush(grad))
            p.setPen(Qt.PenStyle.NoPen)
            p.drawRoundedRect(QRectF(x, y, w * frac, h), h // 2, h // 2)

        lbl_sz = max(7, int(9 * scale))
        p.setFont(QFont("Arial", lbl_sz, QFont.Weight.Bold))
        p.setPen(QPen(QColor(255, 255, 255, 200)))
        p.drawText(QRectF(x + 5, y, w - 10, h),
                   Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, label)

    def _draw_overlay(self, p, W, H, title, subtitle, btns_hint, tc):
        overlay = QColor(0, 0, 0, 170)
        p.fillRect(0, 0, W, H, overlay)
        card_w = min(400, W - 60)
        card_h = 260
        cx = (W - card_w) // 2
        cy = (H - card_h) // 2
        card_col = QColor(tc["card"])
        card_col.setAlpha(240)
        p.setBrush(QBrush(card_col))
        p.setPen(QPen(QColor(tc["accent"]), 2))
        p.drawRoundedRect(QRectF(cx, cy, card_w, card_h), 16, 16)

        p.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        p.setPen(QPen(QColor(tc["accent"])))
        p.drawText(QRectF(cx, cy + 28, card_w, 50), Qt.AlignmentFlag.AlignCenter, title)

        p.setFont(QFont("Arial", 13))
        p.setPen(QPen(QColor(tc["text2"])))
        p.drawText(QRectF(cx, cy + 85, card_w, 40), Qt.AlignmentFlag.AlignCenter, subtitle)

        p.setFont(QFont("Arial", 11))
        p.setPen(QPen(QColor(tc["text2"])))
        p.drawText(QRectF(cx, cy + card_h - 55, card_w, 30), Qt.AlignmentFlag.AlignCenter, btns_hint)

    def _draw_pause(self, p, W, H, tc):
        self._draw_overlay(
            p, W, H,
            self.t("pause"),
            f"{self.t('score')}: {self.hero.score if self.hero else 0}",
            f"[R] {self.t('resume')}   [M] {self.t('main_menu')}",
            tc
        )

    def _draw_game_over(self, p, W, H, tc):
        self._draw_overlay(
            p, W, H,
            self.t("game_over"),
            f"{self.t('score')}: {self.hero.score if self.hero else 0}  |  {self.t('kills')}: {self.hero.kills if self.hero else 0}",
            f"[R] {self.t('restart')}   [M] {self.t('main_menu')}",
            tc
        )

    def _draw_victory(self, p, W, H, tc):
        self._draw_overlay(
            p, W, H,
            self.t("victory"),
            f"{self.t('score')}: {self.hero.score if self.hero else 0}  |  {self.t('kills')}: {self.hero.kills if self.hero else 0}",
            f"[R] {self.t('restart')}   [M] {self.t('main_menu')}",
            tc
        )

    # ── INPUT ──
    def keyPressEvent(self, event):
        self.keys.add(event.key())
        k = event.key()

        if self.game_over or self.victory:
            if k == Qt.Key.Key_R:
                self.request_restart.emit()
            elif k == Qt.Key.Key_M:
                self.request_menu.emit()
            return

        if k == Qt.Key.Key_Escape or k == Qt.Key.Key_P:
            self.paused = not self.paused

        if self.paused:
            if k == Qt.Key.Key_R:
                self.paused = False
            elif k == Qt.Key.Key_M:
                self.request_menu.emit()
            return

        if k == Qt.Key.Key_Space:
            self._attack()
        if k == Qt.Key.Key_Shift:
            self._dash()
        if k == Qt.Key.Key_E:
            self._spell()

    def keyReleaseEvent(self, event):
        self.keys.discard(event.key())

    def mouseMoveEvent(self, event):
        self.mouse_pos = event.position()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if not self.paused and not self.game_over and not self.victory:
                self._attack()
        elif event.button() == Qt.MouseButton.RightButton:
            if not self.paused and not self.game_over and not self.victory:
                self._spell()


# ─────────────────────────── SETTINGS PAGE ───────────────────────────
class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self.lang = "en"
        self.on_back = None
        self.on_theme = None
        self.on_lang = None
        self._build()

    def t(self, k): return TR[self.lang].get(k, k)
    def tc(self): return TH[self.theme]

    def _build(self):
        for ch in self.children():
            if isinstance(ch, QWidget):
                ch.deleteLater()

        tc = self.tc()

        if hasattr(self, "_outer"):
            old = self._outer
            self.setLayout(None)
            old.deleteLater()

        self._outer = QVBoxLayout(self)
        self._outer.setContentsMargins(0, 0, 0, 0)
        self._outer.setSpacing(0)

        card = QWidget()
        card.setFixedWidth(420)
        card_shadow = QGraphicsDropShadowEffect()
        card_shadow.setBlurRadius(40)
        card_shadow.setColor(QColor(0, 0, 0, 120))
        card_shadow.setOffset(0, 8)
        card.setGraphicsEffect(card_shadow)
        card.setStyleSheet(f"""
            QWidget {{
                background:{tc['card']};
                border-radius:18px;
            }}
        """)
        vb = QVBoxLayout(card)
        vb.setSpacing(18)
        vb.setContentsMargins(36, 36, 36, 36)

        title = QLabel(self.t("settings"))
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color:{tc['accent']};background:transparent;")
        vb.addWidget(title)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet(f"background:{tc['border']};max-height:1px;border:none;")
        vb.addWidget(sep)

        label_style = f"color:{tc['text']};background:transparent;font-size:14px;font-weight:bold;"
        combo_style = f"""
            QComboBox {{
                background:{tc['btn']};
                color:{tc['text']};
                border:1.5px solid {tc['accent']};
                border-radius:8px;
                padding:6px 12px;
                font-size:13px;
                min-width:130px;
            }}
            QComboBox::drop-down {{border:none;}}
            QComboBox QAbstractItemView {{
                background:{tc['card2']};
                color:{tc['text']};
                border:1px solid {tc['border']};
                selection-background-color:{tc['accent']};
                selection-color:#fff;
            }}
        """

        def make_row(label_text, widget):
            row = QHBoxLayout()
            lbl = QLabel(label_text)
            lbl.setFont(QFont("Arial", 13, QFont.Weight.Bold))
            lbl.setStyleSheet(label_style)
            row.addWidget(lbl)
            row.addStretch()
            row.addWidget(widget)
            return row

        # Theme
        self._theme_cb = QComboBox()
        self._theme_cb.addItem(self.t("dark"), "dark")
        self._theme_cb.addItem(self.t("light"), "light")
        self._theme_cb.setCurrentIndex(0 if self.theme == "dark" else 1)
        self._theme_cb.setStyleSheet(combo_style)
        vb.addLayout(make_row(self.t("theme"), self._theme_cb))

        # Language
        self._lang_cb = QComboBox()
        self._lang_cb.addItem("English", "en")
        self._lang_cb.addItem("中文", "zh")
        self._lang_cb.addItem("فارسی", "fa")
        idx = {"en": 0, "zh": 1, "fa": 2}.get(self.lang, 0)
        self._lang_cb.setCurrentIndex(idx)
        self._lang_cb.setStyleSheet(combo_style)
        vb.addLayout(make_row(self.t("language"), self._lang_cb))

        vb.addSpacing(8)

        btn_style = f"""
            QPushButton {{
                background:{tc['btn']};
                color:{tc['btn_text']};
                border:2px solid {tc['accent']};
                border-radius:10px;
                font-size:14px;
                font-weight:bold;
                padding:10px 20px;
            }}
            QPushButton:hover {{
                background:{tc['btn_hover']};
                color:#ffffff;
                border-color:{tc['accent2']};
            }}
        """

        apply_btn = QPushButton(self.t("apply"))
        apply_btn.setFont(QFont("Arial", 13, QFont.Weight.Bold))
        apply_btn.setMinimumHeight(44)
        apply_btn.setStyleSheet(btn_style)
        apply_btn.clicked.connect(self._apply)
        vb.addWidget(apply_btn)

        back_btn = QPushButton(self.t("back"))
        back_btn.setFont(QFont("Arial", 13, QFont.Weight.Bold))
        back_btn.setMinimumHeight(44)
        back_btn.setStyleSheet(btn_style)
        back_btn.clicked.connect(lambda: self.on_back() if self.on_back else None)
        vb.addWidget(back_btn)

        self._outer.addStretch(1)
        row_h = QHBoxLayout()
        row_h.addStretch()
        row_h.addWidget(card)
        row_h.addStretch()
        self._outer.addLayout(row_h)
        self._outer.addStretch(1)

    def _apply(self):
        t = self._theme_cb.currentData()
        l = self._lang_cb.currentData()
        if self.on_theme and t != self.theme:
            self.on_theme(t)
        if self.on_lang and l != self.lang:
            self.on_lang(l)

    def refresh(self):
        self._build()

    def paintEvent(self, event):
        W, H = self.width(), self.height()
        p = QPainter(self)
        tc = self.tc()
        grad = QLinearGradient(0, 0, W, H)
        grad.setColorAt(0, QColor(tc["bg"]))
        grad.setColorAt(0.6, QColor(tc["bg2"]))
        grad.setColorAt(1, QColor(tc["bg3"]))
        p.fillRect(0, 0, W, H, QBrush(grad))
        p.end()


# ─────────────────────────── WORLD SELECT ───────────────────────────
class WorldSelectDialog(QDialog):
    def __init__(self, parent=None, theme="dark", lang="en"):
        super().__init__(parent)
        self.theme = theme
        self.lang = lang
        self.chosen_world = "forest"
        self.chosen_diff = "normal"
        self.setModal(True)
        self.setMinimumWidth(380)
        self.setWindowTitle(TR[lang].get("world_select", "Select World"))
        self._build()

    def t(self, k): return TR[self.lang].get(k, k)
    def tc(self): return TH[self.theme]

    def _build(self):
        tc = self.tc()
        self.setStyleSheet(f"""
            QDialog {{background:{tc['card']};border-radius:16px;}}
            QLabel {{color:{tc['text']};background:transparent;}}
            QComboBox {{
                background:{tc['btn']};color:{tc['text']};
                border:1.5px solid {tc['accent']};border-radius:8px;
                padding:6px 12px;font-size:13px;min-width:140px;
            }}
            QComboBox::drop-down {{border:none;}}
            QComboBox QAbstractItemView {{
                background:{tc['card2']};color:{tc['text']};
                border:1px solid {tc['border']};
                selection-background-color:{tc['accent']};selection-color:#fff;
            }}
        """)
        layout = QVBoxLayout(self)
        layout.setSpacing(18)
        layout.setContentsMargins(32, 32, 32, 32)

        title = QLabel(self.t("world_select"))
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color:{tc['accent']};")
        layout.addWidget(title)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet(f"background:{tc['border']};max-height:1px;border:none;")
        layout.addWidget(sep)

        def row(label, widget):
            r = QHBoxLayout()
            lbl = QLabel(label)
            lbl.setFont(QFont("Arial", 13, QFont.Weight.Bold))
            r.addWidget(lbl)
            r.addStretch()
            r.addWidget(widget)
            return r

        self._world_cb = QComboBox()
        self._world_cb.addItem(self.t("forest"), "forest")
        self._world_cb.addItem(self.t("dungeon"), "dungeon")
        self._world_cb.addItem(self.t("castle"), "castle")
        layout.addLayout(row(self.t("world_select"), self._world_cb))

        self._diff_cb = QComboBox()
        self._diff_cb.addItem(self.t("easy"), "easy")
        self._diff_cb.addItem(self.t("normal"), "normal")
        self._diff_cb.addItem(self.t("hard"), "hard")
        self._diff_cb.setCurrentIndex(1)
        layout.addLayout(row(self.t("difficulty"), self._diff_cb))

        layout.addSpacing(8)
        btn_style = f"""
            QPushButton {{
                background:{tc['btn']};color:{tc['btn_text']};
                border:2px solid {tc['accent']};border-radius:10px;
                font-size:13px;font-weight:bold;padding:9px 22px;
            }}
            QPushButton:hover {{background:{tc['btn_hover']};color:#fff;}}
        """
        btn_row = QHBoxLayout()
        cancel = QPushButton(self.t("cancel"))
        cancel.setStyleSheet(btn_style)
        cancel.clicked.connect(self.reject)
        start = QPushButton(self.t("play"))
        start.setStyleSheet(btn_style)
        start.clicked.connect(self._accept)
        btn_row.addWidget(cancel)
        btn_row.addStretch()
        btn_row.addWidget(start)
        layout.addLayout(btn_row)

    def _accept(self):
        self.chosen_world = self._world_cb.currentData()
        self.chosen_diff = self._diff_cb.currentData()
        self.accept()


# ─────────────────────────── MAIN MENU ───────────────────────────
class MainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self.lang = "en"
        self.on_play = None
        self.on_settings = None
        self.on_exit = None
        self._anim_t = 0.0
        self._anim_timer = QTimer(self)
        self._anim_timer.timeout.connect(self._anim_step)
        self._anim_timer.start(33)
        self._particles = [(random.uniform(0, 1), random.uniform(0, 1),
                            random.uniform(-0.02, 0.02), random.uniform(-0.04, -0.01),
                            random.uniform(2, 5)) for _ in range(40)]
        self._build()

    def t(self, k): return TR[self.lang].get(k, k)
    def tc(self): return TH[self.theme]

    def _anim_step(self):
        self._anim_t += 0.033
        parts = []
        for x, y, vx, vy, sz in self._particles:
            x += vx * 0.016
            y += vy * 0.016
            if y < -0.05 or x < -0.05 or x > 1.05:
                x = random.uniform(0, 1)
                y = random.uniform(0.9, 1.1)
                vy = random.uniform(-0.04, -0.01)
            parts.append((x, y, vx, vy, sz))
        self._particles = parts
        self.update()

    def _build(self):
        for ch in self.findChildren(QWidget):
            ch.deleteLater()
        tc = self.tc()

        main = QVBoxLayout(self)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(0)
        main.addStretch(2)

        center = QHBoxLayout()
        center.addStretch()

        card = QWidget()
        card.setFixedWidth(340)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(60)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setOffset(0, 12)
        card.setGraphicsEffect(shadow)
        card.setStyleSheet(f"background:rgba(0,0,0,0);border-radius:22px;")

        vb = QVBoxLayout(card)
        vb.setSpacing(14)
        vb.setContentsMargins(36, 40, 36, 40)

        title = QLabel(self.t("title"))
        title.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color:{tc['accent']};background:transparent;letter-spacing:2px;")
        vb.addWidget(title)

        sub = QLabel("◈  Action Adventure  ◈")
        sub.setFont(QFont("Arial", 11))
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub.setStyleSheet(f"color:{tc['text2']};background:transparent;")
        vb.addWidget(sub)
        vb.addSpacing(10)

        btn_style = f"""
            QPushButton {{
                background:qlineargradient(x1:0,y1:0,x2:1,y2:0,
                    stop:0 {tc['btn']}, stop:1 {tc['card2']});
                color:{tc['btn_text']};
                border:1.5px solid {tc['accent']};
                border-radius:12px;
                font-size:15px;
                font-weight:bold;
                padding:12px 0px;
                letter-spacing:1px;
            }}
            QPushButton:hover {{
                background:qlineargradient(x1:0,y1:0,x2:1,y2:0,
                    stop:0 {tc['accent']}, stop:1 {tc['btn_hover']});
                color:#ffffff;
                border-color:{tc['accent2']};
            }}
            QPushButton:pressed {{
                background:{tc['btn_hover']};
            }}
        """

        for key, callback_attr in [
            ("play", "on_play"),
            ("settings", "on_settings"),
            ("exit", "on_exit"),
        ]:
            btn = QPushButton(self.t(key))
            btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            btn.setMinimumHeight(48)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            btn.setStyleSheet(btn_style)
            attr = callback_attr
            btn.clicked.connect(lambda checked=False, a=attr: getattr(self, a)() if getattr(self, a) else None)
            vb.addWidget(btn)

        vb.addSpacing(8)
        ver = QLabel("v1.0  |  PyQt6")
        ver.setFont(QFont("Arial", 9))
        ver.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ver.setStyleSheet(f"color:{tc['text2']};background:transparent;")
        vb.addWidget(ver)

        center.addWidget(card)
        center.addStretch()
        main.addLayout(center)
        main.addStretch(3)

    def refresh(self):
        self._build()

    def paintEvent(self, event):
        W, H = self.width(), self.height()
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        tc = self.tc()

        # Background gradient
        grad = QLinearGradient(0, 0, W * 0.5, H)
        grad.setColorAt(0, QColor(tc["bg"]))
        grad.setColorAt(0.5, QColor(tc["bg2"]))
        grad.setColorAt(1, QColor(tc["bg3"]))
        p.fillRect(0, 0, W, H, QBrush(grad))

        # Animated orb background
        t = self._anim_t
        for i, (ox, oy, r, col) in enumerate([
            (0.2, 0.3, 0.25, tc["accent"]),
            (0.8, 0.6, 0.2, tc["accent2"]),
            (0.5, 0.8, 0.18, tc["accent3"]),
        ]):
            px = ox + math.sin(t * 0.4 + i * 1.3) * 0.06
            py = oy + math.cos(t * 0.3 + i * 2.1) * 0.05
            rad = int(r * min(W, H) * (0.9 + math.sin(t * 0.5 + i) * 0.1))
            base = QColor(col)
            base.setAlpha(18)
            rg = QRadialGradient(QPointF(px * W, py * H), rad)
            rg.setColorAt(0, base)
            base2 = QColor(col)
            base2.setAlpha(0)
            rg.setColorAt(1, base2)
            p.fillRect(0, 0, W, H, QBrush(rg))

        # Floating particles
        for (px, py, vx, vy, sz) in self._particles:
            pc = QColor(tc["accent"])
            pc.setAlpha(80)
            p.setBrush(QBrush(pc))
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(QPointF(px * W, py * H), sz, sz)

        # Decorative circles
        p.setPen(QPen(QColor(tc["accent"]), 1))
        p.setBrush(Qt.BrushStyle.NoBrush)
        cx, cy_val = W // 2, H // 2
        for ri in range(3):
            alpha = 20 + ri * 12
            col = QColor(tc["accent"])
            col.setAlpha(alpha)
            p.setPen(QPen(col, 1))
            offset = math.sin(t * 0.5 + ri) * 10
            rad2 = int((200 + ri * 120 + offset) * min(W, H) / 800)
            p.drawEllipse(QPointF(cx, cy_val), rad2, rad2)

        p.end()


# ─────────────────────────── MAIN APP ───────────────────────────
class AdventureApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme = "dark"
        self.lang = "en"
        self._last_world = "forest"
        self._last_diff = "normal"
        self.setWindowTitle(TR[self.lang]["title"])
        self.setMinimumSize(700, 480)
        self.resize(1100, 720)

        self._stack = QStackedWidget()
        self.setCentralWidget(self._stack)

        self._menu = MainMenu()
        self._settings_pg = SettingsPage()
        self._game_renderer = GameRenderer()

        self._stack.addWidget(self._menu)
        self._stack.addWidget(self._settings_pg)
        self._stack.addWidget(self._game_renderer)

        self._menu.on_play = self._show_world_select
        self._menu.on_settings = self._show_settings
        self._menu.on_exit = self.close

        self._settings_pg.on_back = self._show_menu
        self._settings_pg.on_theme = self._change_theme
        self._settings_pg.on_lang = self._change_lang

        self._game_renderer.request_menu.connect(self._show_menu)
        self._game_renderer.request_restart.connect(self._restart_game)

        self._apply_theme()
        self._stack.setCurrentIndex(0)

    def _show_menu(self):
        self._stack.setCurrentIndex(0)

    def _show_settings(self):
        self._settings_pg.theme = self.theme
        self._settings_pg.lang = self.lang
        self._settings_pg.refresh()
        self._stack.setCurrentIndex(1)

    def _show_world_select(self):
        dlg = WorldSelectDialog(self, theme=self.theme, lang=self.lang)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self._last_world = dlg.chosen_world
            self._last_diff = dlg.chosen_diff
            self._start_game(self._last_world, self._last_diff)

    def _start_game(self, wtype, diff):
        prog = QProgressDialog(
            TR[self.lang].get("generating", "Loading…"),
            None, 0, 0, self
        )
        prog.setWindowModality(Qt.WindowModality.WindowModal)
        prog.setWindowTitle(TR[self.lang].get("generating", "Loading"))
        prog.setMinimumDuration(0)
        prog.setStyleSheet(f"""
            QProgressDialog {{
                background:{TH[self.theme]['card']};
                color:{TH[self.theme]['text']};
                border-radius:12px;
            }}
            QLabel {{color:{TH[self.theme]['text']};}}
        """)
        prog.show()
        QApplication.processEvents()

        self._game_renderer.theme = self.theme
        self._game_renderer.lang = self.lang
        self._game_renderer.start_game(wtype, diff)

        prog.close()
        self._stack.setCurrentIndex(2)
        self._game_renderer.setFocus()

    def _restart_game(self):
        self._start_game(self._last_world, self._last_diff)

    def _change_theme(self, t):
        self.theme = t
        self._apply_theme()
        self._menu.theme = t
        self._menu.refresh()
        self._settings_pg.theme = t
        self._settings_pg.refresh()
        self._game_renderer.theme = t

    def _change_lang(self, l):
        self.lang = l
        self.setWindowTitle(TR[l]["title"])
        self._menu.lang = l
        self._menu.refresh()
        self._settings_pg.lang = l
        self._settings_pg.refresh()
        self._game_renderer.lang = l

    def _apply_theme(self):
        tc = TH[self.theme]
        self.setStyleSheet(f"QMainWindow {{ background:{tc['bg']}; }}")

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def closeEvent(self, event):
        tc = TH[self.theme]
        msg = QMessageBox(self)
        msg.setWindowTitle(TR[self.lang].get("exit", "Exit"))
        msg.setText(self.t("exit") + "?")
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        msg.setStyleSheet(f"""
            QMessageBox {{
                background:{tc['card']};
                color:{tc['text']};
                border-radius:12px;
            }}
            QLabel {{
                color:{tc['text']};
                font-size:14px;
            }}
            QPushButton {{
                background:{tc['btn']};
                color:{tc['btn_text']};
                border:1.5px solid {tc['accent']};
                border-radius:8px;
                padding:7px 18px;
                font-size:13px;
                font-weight:bold;
                min-width:70px;
            }}
            QPushButton:hover {{
                background:{tc['btn_hover']};
                color:#ffffff;
            }}
        """)
        if msg.exec() == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def t(self, k):
        return TR[self.lang].get(k, k)


# ─────────────────────────── ENTRY POINT ───────────────────────────
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Shadow Realm")
    app.setStyle("Fusion")

    try:
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    except AttributeError:
        pass

    win = AdventureApp()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
