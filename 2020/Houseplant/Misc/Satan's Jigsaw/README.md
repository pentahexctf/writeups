# Houseplant CTF – Satan's Jigsaw

* **Category:** Misc.
* **Points:** 704 Points

## Challenge

> Oh no! I dropped my pixels on the floor and they're all muddled up! It's going to take me years to sort all 90,000 of these again :(
>
> Dev: Tom
> 
> Hint! long_to_bytes

(chall.7z was attached)

## Solution

Upon extracting the archive, we find *a lot* of images. To be exact: 90,000 images. Each one appears to be a single pixel, and running long_to_bytes on the file names appears to return two integers. We surmise that these are the coordinates of each pixel.

Since there's 90000 pixels, we assume the the image size is 300x300. I wrote a godawful script to place each pixel in its corresponding location.

The output image contains two QR codes, one of which is the flag. The other is a rickroll, because Rick is never going to give us up.

```
rtcp{d1d-you_d0_7his_by_h4nd?}
```
