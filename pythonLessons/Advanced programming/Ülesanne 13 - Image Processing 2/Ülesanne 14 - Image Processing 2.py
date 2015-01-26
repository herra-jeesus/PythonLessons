"""
Ülesanne 14 - Image processing 2
Juhend: https://courses.cs.ttu.ee/w/images/2/20/2014_Loeng_13_-_Image_processing_2.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

from PIL import Image
import math
import colorsys
import numpy

def generate_gradient_color_space(gradient):
    # convert RGB to HSV

    gradient_hsv = {}

    for x, color in gradient.items():
        gradient_hsv[x] = colorsys.rgb_to_hsv(color[0], color[1], color[2])

    # generate gradient color space using linear interpolation

    x = numpy.linspace(0, 1, 2048)
    xp = sorted(gradient_hsv.keys())
    fp = [gradient_hsv[x] for x in xp]
    h = [color[0] for color in fp]
    s = [color[1] for color in fp]
    v = [color[2] for color in fp]
    h_interp = numpy.interp(x, xp, h)
    s_interp = numpy.interp(x, xp, s)
    v_interp = numpy.interp(x, xp, v)
    result_gradient = {}

    # convert HSV back to RGB

    for i in range(2048):
        result_gradient[i] = colorsys.hsv_to_rgb(h_interp[i], s_interp[i], v_interp[i])

    return result_gradient

def mandelbrot(size, iterations):
    gradient = {
        0.0     : (  0,   7, 100),
        0.16    : ( 32, 107, 203),
        0.42    : (237, 255, 255),
        0.6425  : (255, 170,   0),
        0.8575  : (  0,   2,   0)
    }

    color_space = generate_gradient_color_space(gradient)
    # Drawing area
    xa = -2.0
    xb = 1.0
    ya = 1.5
    yb = -1.5

    width = size[0]
    height = size[1]

    pixels = []

    for y in range(height):
        cy = ya + (yb - ya) * y / height # scaled to lie in the Mandelbrot Y scale

        for x in range(width):
            cx = xa + (xb - xa) * x / width # scaled to lie in the Mandelbrot X scale
            c = complex(cx, cy)
            z = 0

            for i in range(iterations):
                if abs(z) > 2.0: break # has escaped Mandelbrot set
                z = z * z + c

            if i < iterations-1:
                smoothed = math.log(math.log(abs(z)) / math.log(2)) / math.log(2)
                colorIndex = int(math.sqrt(i + 1 - smoothed) * 256) % len(color_space)
                color = color_space[colorIndex]
                r = int(round(color[0]))
                g = int(round(color[1]))
                b = int(round(color[2]))
                pixels.append((r,g,b))
            else:
                pixels.append((0,0,0))

    print("Mandelbrot finished generating.")
    return pixels

def julia(c, size, iterations):

    gradient = {
        0.0     : (  0,   7, 100),
        0.16    : ( 32, 107, 203),
        0.42    : (237, 255, 255),
        0.6425  : (255, 170,   0),
        0.8575  : (  0,   2,   0)
    }

    color_space = generate_gradient_color_space(gradient)

    # drawing area
    xa = -1.5
    xb = 1.5
    ya = 1.5
    yb = -1.5

    width = size[0]
    height = size[1]

    pixels = []

    for y in range(height):
        zy = ya + (yb - ya) * y / height # scaled to lie in the Mandelbrot Y scale

        for x in range(width):
            zx = xa + (xb - xa) * x / width # scaled to lie in the Mandelbrot X scale
            z = complex(zx, zy)

            for i in range(iterations):
                if abs(z) > 2.0: break # has escaped Mandelbrot set
                z = z * z + c

            if i < iterations-1:
                smoothed = math.log(math.log(abs(z)) / math.log(2)) / math.log(2)
                colorIndex = int(math.sqrt(i + 1 - smoothed) * 256) % len(color_space)
                color = color_space[colorIndex]
                r = int(round(color[0]))
                g = int(round(color[1]))
                b = int(round(color[2]))
                pixels.append((r,g,b))
            else:
                pixels.append((0,0,0))

    print("Julia finished generating.")
    return pixels

def image_from_pixels(size, pixels, fileName):
    img = Image.new("RGB", size)
    img.putdata(pixels)
    img.save(fileName)

def main():
    # Create Mandelbrot set
    size = (1024, 1024)
    pixels = mandelbrot(size, 256)
    image_from_pixels(size, pixels, "Mandelbrot.png")

    # Create julia1
    size = (512, 512)
    pixels = julia(-0.4+0.6j, size, 256)
    image_from_pixels(size, pixels, "julia1.png")

    # Create julia2
    pixels = julia(0.285+0.01j, size, 256)
    image_from_pixels(size, pixels, "julia2.png")

    # Create julia3
    pixels = julia(-0.70176-0.3842j, size, 256)
    image_from_pixels(size, pixels, "julia3.png")

    # Create julia4
    pixels = julia(-0.8+0.156j, size, 256)
    image_from_pixels(size, pixels, "julia4.png")

    print("All done.")

if __name__ == "__main__":
    main()