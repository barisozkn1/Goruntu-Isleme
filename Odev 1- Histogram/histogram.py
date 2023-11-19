import cv2
from matplotlib import pyplot as plt

def calculate_histogram(image):
    height, width = image.shape
    histogram = [0] * 256
    for y in range(height):
        for x in range(width):
            pixel_value = image[y, x]
            histogram[pixel_value] += 1

    return histogram
image_name = "C:\\Users\\baris\\Desktop\\asdasd.jpg"
image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

if image is not None:
    histogram = calculate_histogram(image)
    plt.bar(range(256), histogram)
    plt.title("Histogram")
    plt.xlabel("Piksel Değeri")
    plt.ylabel("Piksel Sayısı")
    plt.show()


else:
    print("Görüntü okunamadı. Lütfen dosya yolunu kontrol edin.")