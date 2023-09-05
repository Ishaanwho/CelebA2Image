import pygame
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt


# Initialize Pygame
pygame.init()

# Set up the window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Text-to-Image Generation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Font settings
font = pygame.font.Font(None, 28)
input_font = pygame.font.Font(None, 24)

# Other constants
INPUT_BOX_WIDTH = 600
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

# Load the USE model 
use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Define the noise vector dimensions
latent_dim = 100
# Load the trained generator model
generator = tf.keras.models.load_model('generator_model.h5')

# Define attribute names
attribute_names = ['Bangs', 'Eyeglasses', 'No_Beard', 'Smiling', 'Young']
num_attributes = len(attribute_names)

# Attribute descriptions
attribute_descriptions = {
    "Bangs": [
        "Has no bangs. Can see 100% of the forehead.",
        "Has very short bangs. Can see 80% of the forehead.",
        "Has middle short bangs. Can see 60% of the forehead.",
        "Has middle-length bangs. Can see 40% of the forehead.",
        "Has middle long bangs. Can see 20% of the forehead.",
        "Has long bangs. Can see 0% of the forehead."
    ],
    "Eyeglasses": [
        "No eyeglasses.",
        "With/wearing eyeglasses that are rimless or have very thin metal frames.",
        "With/wearing eyeglasses that have middle-thickness metal frames or thin plastic frames.",
        "With/wearing eyeglasses that have thick plastic frames.",
        "With/wearing thin-frame sunglasses.",
        "With/wearing thick-frame sunglasses."
    ],
    "No_Beard": [
        "Has no beard.",
        "Has a beard that is just shaved and very short. Short beard, stubble.",
        "Hasn't shaved for a while and has a middle-short beard. Medium-short beard",
        "Has grown a beard that is middle-length. Medium beard",
        "Has grown a beard that is long and well-groomed. Big, long Beard",
        "Has a bushy beard that is long and not groomed. Huge beard, not maintained."
    ],
    "Smiling": [
        "Is not smiling.",
        "Has a small smile. Cannot see the teeth.",
        "Has a bright smile. Can see some teeth.",
        "Is smiling. Can see the entire row of teeth.",
        "Has a big smile. Can see the entire row of teeth. The mouth is slightly open.",
        "Has a very big smile. Can see the entire row of teeth. The mouth is fully open."
    ],
    "Young": [
        "Age is less than 15 years old. Has a childlike look on the face.",
        "Age is between 15 and 20 years old. Teenager.",
        "Age is between 20 and 40 years old. Young adults.",
        "Age is between 40 and 50 years old. Middle-aged.",
        "Age is between 50 and 60 years old. Aged.",
        "Age is above 60. Elderly."
    ]
}

# Function to compare input text to attribute description
def compare_to_attributes(text_input, similarity_threshold=0.35, default_value=0):
    attribute_intensities = []

    for attribute, descriptions in attribute_descriptions.items():
        description_embeddings = use_model(descriptions).numpy()
        similarities = cosine_similarity([text_input], description_embeddings)
        
        # Find the index of the closest matching description
        closest_index = np.argmax(similarities)
        
        # Check if the similarity is above the threshold
        if similarities[0, closest_index] > similarity_threshold:
            attribute_value = closest_index  # Assign the attribute value based on the index
        else:
            attribute_value = default_value  # Assign a default value if similarity is below threshold
        
        attribute_intensities.append(attribute_value)

    gen_attributes = np.array([attribute_intensities])
    return gen_attributes

#Encode the textual description using USE
def pre_process_input(text):
    text_embedding = use_model([text])[0].numpy()
    return text_embedding  
    
    
# Function to generate the image
def generate_image(text_input):
    # Calculate cosine similarity between input_embedding and attribute_descriptions
    final_attributes = compare_to_attributes(text_input)
    print(final_attributes)
    # Generate noise vector
    noise_vector = np.random.randn(1, latent_dim)
    final_input = np.concatenate([noise_vector, final_attributes], axis = 1)
    
    # Generate image using the generator model
    generated_image = generator.predict(final_input)
    
    return generated_image

def beautify_text(text, font, color):
    return font.render(text, True, color)



# Main game loop
running = True
clock = pygame.time.Clock()

user_input = ""
generated_surface = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            if generate_button.collidepoint(mouse_pos):
                try:       
                  
                    # Preprocess the user input
                    preprocessed_input = pre_process_input(user_input)
                    
                    # Generate image from preprocessed input
                    generated_image = generate_image(preprocessed_input)         
                                        
                    # Display the generated image using matplotlib
                    generated_image_final = np.rot90(np.transpose(generated_image[0], (1, 0, 2)), k=-1)
                    # The generated image had to be rotated 90 degrees
                    plt.imshow(generated_image_final)
                    plt.axis('off')  # Turn off axis labels and ticks
                    plt.show()
                except Exception as e:  
                    print('Error encountered while generating the image:', e)    

    # Clear the window
    window.fill(WHITE)

    # Render input box
    pygame.draw.rect(window, GRAY, (100, 80, INPUT_BOX_WIDTH, 40))
    pygame.draw.rect(window, BLACK, (100, 80, INPUT_BOX_WIDTH, 40), 2)
    user_input_surface = input_font.render(user_input, True, BLACK)
    window.blit(user_input_surface, (110, 80))

    # Render the text description
    text_surface = beautify_text("Enter the description. (Use smile, age, beard, bangs and eyeglasses!):", font, BLACK)
    window.blit(text_surface, (80, 20))
    
    # Clear and generate button position
    clear_button_x = 320
    clear_button_y = 200
    
    generate_button_x = 320
    generate_button_y = 140

    # Define the position and dimensions of the clear button
    clear_button = pygame.Rect(clear_button_x, clear_button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
    generate_button = pygame.Rect(generate_button_x, generate_button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
    
    # Display the clear button
    pygame.draw.rect(window, BLACK, clear_button)
    pygame.draw.rect(window, BLACK, generate_button)

    # Clear button text
    clear_text = beautify_text("Clear Text", font, WHITE)
    generate_text = beautify_text("GENERATE", font, WHITE)

    # Calculate text position within the button
    text_x = clear_button_x + (BUTTON_WIDTH - clear_text.get_width()) // 2
    text_y = clear_button_y + (BUTTON_HEIGHT - clear_text.get_height()) // 2
    
    text_a = generate_button_x + (BUTTON_WIDTH - generate_text.get_width()) // 2
    text_b = generate_button_y + (BUTTON_HEIGHT - generate_text.get_height()) // 2

    # Display the clear button text
    window.blit(clear_text, (text_x, text_y))
    window.blit(generate_text, (text_a, text_b))
    
    # Update the display
    pygame.display.update()
    clock.tick(30)  # Limit the frame rate to 30 FPS

    # Handle button click
    mouse_pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if clear_button.collidepoint(mouse_pos):
            generated_surface = None
            user_input = ""
            

# Quit the game
pygame.quit()
