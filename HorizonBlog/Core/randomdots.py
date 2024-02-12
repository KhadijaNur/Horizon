import pygame
import random
import imageio

# Initialize Pygame
pygame.init()

# Set up display with a wider screen
width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wider Moving Circles GIF")

# Define colors
color1 = (251, 161, 183)   # RGB for #FBA1B7
color2 = (255, 209, 218)   # RGB for #FFD1DA
color3 = (178, 164, 255)   # RGB for #B2A4FF

# Number of circles
num_circles = 40

# Circle parameters with adjusted initial positions
circles = [{'x': random.randint(0, width),
            'y': random.randint(0, height),
            'radius': random.randint(5, 30),
            'color': random.choice([color1, color2, color3]),
            'velocity': (random.uniform(0.5, 1), random.uniform(0.5, 1))}
           for _ in range(num_circles)]

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main loop
running = True
frame_count = 0

# Create a writer for the GIF
with imageio.get_writer('moving_circles_wide.gif', duration=0.1) as writer:
    while running and frame_count < 120:  # Set a limit of 120 frames for the GIF
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill("#F8F0E6")  # White background

        # Draw and move circles slowly
        for circle in circles:
            pygame.draw.circle(screen, circle['color'], (int(circle['x']), int(circle['y'])), circle['radius'])

            # Update circle position
            circle['x'] += circle['velocity'][0]
            circle['y'] += circle['velocity'][1]

            # Bounce off the screen edges
            if circle['x'] <= 0 or circle['x'] >= width:
                circle['velocity'] = (-circle['velocity'][0], circle['velocity'][1])
            if circle['y'] <= 0 or circle['y'] >= height:
                circle['velocity'] = (circle['velocity'][0], -circle['velocity'][1])

        # Update the display
        pygame.display.flip()

        # Convert the current screen to an image and append to the GIF
        image = pygame.surfarray.array3d(pygame.display.get_surface())
        writer.append_data(image)

        # Control the frame rate for slower movement
        clock.tick(15)  # Set the frame rate to 15 frames per second for slower movement

        frame_count += 1

# Quit Pygame
pygame.quit()
