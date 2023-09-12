import cv2
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import time

device = "cuda"

img = cv2.imread("models/riga.jpg")




sam = sam_model_registry["vit_b"](checkpoint="models/sam_vit_b_01ec64.pth")
sam.to(device=device)

mask_generator = SamAutomaticMaskGenerator(sam)

t0 = time.time()
masks = mask_generator.generate(img)
t1 = time.time()

tot_time = (t1-t0) * 1000.0
print("%f.4 ms" % tot_time)


#print(masks)