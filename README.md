## Raychel

For running Raychel, just use the following command:
```bash
python main.py [filename]
```
`filename` is optional (the default is `img`) and the file format is always `.ppm`.

## Unit Tests

```bash
python -m unittest tests. unittests
```

## Current State

> Current: 9.4. True Lambertian Reflection (Ray Tracing In One Weekend)

> Upcoming: 9.5. Using Gamma Correction for Accurate Color Intensity (Ray Tracing In One Weekend)

This is a python implementation of the project(s) from the book series [Ray Tracing In One Weekend](https://raytracing.github.io)

## Renders

Inside the `renders` directory, there are all renders from the book, made by Raychel. As mentioned above, the file format is `.ppm`.

### Diffuse Spheres

There are several renders with diffuse spheres. In this section, I'd like to talk about the differences between `diffuse-sphere-without-shadow-acne.ppm` (before) and `diffuse-lambertian-sphere.ppm` (after). The most obvious is the shadow, which is darker again. The book also claims that both spheres "are tinted blue from the sky" now, but I don't really see that much of a difference.
