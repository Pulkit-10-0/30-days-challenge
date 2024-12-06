import easyocr
import matplotlib.pyplot as plt
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)  


image_path = '2.jpg'
results = reader.readtext(image_path)
print("OCR Results:")
for (bbox, text, prob) in results:
    print(f"Detected text: {text} (Confidence: {prob:.2f})")
image = Image.open(image_path)
plt.imshow(image)
plt.axis('off')

for (bbox, text, prob) in results:
    
    coords = [tuple(coord) for coord in bbox]
    plt.plot(
        [coords[0][0], coords[1][0], coords[2][0], coords[3][0], coords[0][0]],
        [coords[0][1], coords[1][1], coords[2][1], coords[3][1], coords[0][1]],
        color='red',
        linewidth=2,
    )
plt.show()