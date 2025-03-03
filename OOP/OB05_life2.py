import pygame
import sys
import random

# Настройки игры
CELL_SIZE = 10  # Размер клетки
GRID_WIDTH = 80  # Количество клеток по горизонтали
GRID_HEIGHT = 60  # Количество клеток по вертикали
FPS = 10  # Частота обновления экрана

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
        self.running = False  # Флаг, идет ли симуляция

    def create_empty_grid(self):
        """Создает пустую сетку."""
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def draw_grid(self, screen):
        """Рисует текущую сетку на экране."""
        for y in range(self.height):
            for x in range(self.width):
                color = WHITE if self.grid[y][x] == 1 else BLACK
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                )
                # Рисуем границы клеток
                pygame.draw.rect(
                    screen,
                    GRAY,
                    pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size),
                    1
                )

    def update_grid(self):
        """Обновляет сетку на основе правил игры."""
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                alive_neighbors = self.count_alive_neighbors(x, y)

                # Правила игры
                if self.grid[y][x] == 1:  # Живая клетка
                    if alive_neighbors in (2, 3):
                        new_grid[y][x] = 1
                else:  # Мертвая клетка
                    if alive_neighbors == 3:
                        new_grid[y][x] = 1

        self.grid = new_grid

    def count_alive_neighbors(self, x, y):
        """Считает количество живых соседей вокруг клетки (x, y)."""
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                count += self.grid[ny][nx]

        return count

    def toggle_cell(self, x, y):
        """Переключает состояние клетки (живой/мертвой)."""
        self.grid[y][x] = 1 if self.grid[y][x] == 0 else 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    # Создаем игру
    game = GameOfLife(GRID_WIDTH, GRID_HEIGHT, CELL_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Запуск/пауза симуляции
                    game.running = not game.running
                elif event.key == pygame.K_c:  # Очистить сетку
                    game.grid = game.create_empty_grid()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not game.running:  # Редактирование доступно только в паузе
                    x, y = event.pos
                    cell_x = x // CELL_SIZE
                    cell_y = y // CELL_SIZE
                    game.toggle_cell(cell_x, cell_y)

        # Обновление игры
        if game.running:
            game.update_grid()

        # Отрисовка игры
        screen.fill(BLACK)
        game.draw_grid(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
