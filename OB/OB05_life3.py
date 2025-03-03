import pygame
import sys

# Настройки игры
CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
FPS = 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)


class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = self.create_empty_grid()
        self.running = False

    def create_empty_grid(self):
        """Создает пустую сетку."""
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def draw_grid(self, screen):
        """Рисует сетку на экране."""
        for y in range(self.height):
            for x in range(self.width):
                color = WHITE if self.grid[y][x] == 1 else BLACK
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size),
                )
                pygame.draw.rect(
                    screen,
                    GRAY,
                    pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size),
                    1,
                )

    def update_grid(self):
        """Обновляет сетку на основе правил игры."""
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                alive_neighbors = self.count_alive_neighbors(x, y)
                if self.grid[y][x] == 1:
                    if alive_neighbors in (2, 3):
                        new_grid[y][x] = 1
                else:
                    if alive_neighbors == 3:
                        new_grid[y][x] = 1
        self.grid = new_grid

    def count_alive_neighbors(self, x, y):
        """Считает количество живых соседей вокруг клетки."""
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                count += self.grid[ny][nx]
        return count

    def insert_pattern(self, pattern, top_left):
        """Добавляет предустановленный паттерн в сетку."""
        px, py = top_left
        for y, row in enumerate(pattern):
            for x, cell in enumerate(row):
                if 0 <= px + x < self.width and 0 <= py + y < self.height:
                    self.grid[py + y][px + x] = cell


def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    # Создаем игру
    game = GameOfLife(GRID_WIDTH, GRID_HEIGHT, CELL_SIZE)

    # Предустановленные паттерны
    patterns = {
        "Glider": [[0, 1, 0], [0, 0, 1], [1, 1, 1]],
        "LWSS": [
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0],
        ],
        "Beacon": [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ],
        "Pulsar": [
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        ],
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.running = not game.running
                elif event.key == pygame.K_c:
                    game.grid = game.create_empty_grid()
                elif event.key in [pygame.K_g, pygame.K_l, pygame.K_b, pygame.K_p]:
                    # Координаты курсора мыши
                    x, y = pygame.mouse.get_pos()
                    cell_x = x // CELL_SIZE
                    cell_y = y // CELL_SIZE

                    # Вставка паттернов
                    if event.key == pygame.K_g:
                        game.insert_pattern(patterns["Glider"], (cell_x, cell_y))
                    elif event.key == pygame.K_l:
                        game.insert_pattern(patterns["LWSS"], (cell_x, cell_y))
                    elif event.key == pygame.K_b:
                        game.insert_pattern(patterns["Beacon"], (cell_x, cell_y))
                    elif event.key == pygame.K_p:
                        game.insert_pattern(patterns["Pulsar"], (cell_x, cell_y))

        if game.running:
            game.update_grid()

        screen.fill(BLACK)
        game.draw_grid(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
