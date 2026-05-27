----------------------------------------
files
----------------------------------------

celeba_dialog
├── celeba_caption
│   └── captions.json
├── celeba_request
│   ├── request_annotated.json
│   ├── request.json
│   └── request.txt
├── combined_annotation.txt
├── metadata.txt
├── test_attr_list.txt
├── train_attr_list.txt
└── val_attr_list.txt

- captions.json: captions for each image
- request_annotated.json: editing request for each image, with hard label annotation
- request.json: editing request for each image, saved in the dictionary form
- request.txt: editing request for each image, saved as plaintext
- combined_annotation.txt: annotation of all images (202599 images = 202578 labeled images + 21 unlabeled images)
- train_attr_list.txt: the train set annotation (162,754 images)
- val_attr_list.txt: the validation set annotation (19,864 images)
- test_attr_list.txt: the test set annotation (19,960 images)

----------------------------------------
Image Download Link
----------------------------------------

https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8?resourcekey=0-5BR16BdXnb8hVj6CNHKzLg

----------------------------------------
Attributes and Annotations
----------------------------------------
Bangs:
0: Has no bangs. Can see 100% of the forehead.
1: Has very short bangs. Can see 80% of the forehead.
2: Has middle short bangs. Can see 60% of the forehead.
3: Has middle-length bangs. Can see 40% of the forehead.
4: Has middle long bangs. Can see 20% of the forehead.
5: Has long bangs. Can see 0% of the forehead.
Eyeglasses:
0: No eyeglasses.
1: With eyeglasses that are rimless or have very thin metal frames.
2: With eyeglasses that have middle-thickness metal frames or thin plastic frames.
3: With eyeglasses that have thick plastic frames.
4: With thin-frame sunglasses.
5: With thick-frame sunglasses.
No_Beard:
0: Has no beard.
1: Has a beard that is just shaved and very short.
2: Hasn't shaved for a while and has a middle-short beard.
3: Has grown a beard that is middle-length.
4: Has grown a beard that is long and well-groomed.
5: Has a bushy beard that is long and not groomed.
Smiling:
0: Is not smiling.
1: Has a small smile. Cannot see the teeth.
2: Has a small smile. Can see some teeth.
3: Is smiling. Can see the entire row of teeth.
4: Has a big smile. Can see the entire row of teeth. The mouth is slightly open.
5: Has a very big smile. Can see the entire row of teeth. The mouth is
Young:
0: Is less than 15 years old. Has a childlike look on the face.
1: Is between 15 and 30 years old. Teenager.
2: Is between 30 and 40 years old. Young adults.
3: Is between 40 and 50 years old. Middle-aged.
4: Is between 50 and 60 years old. Aged.
5: Is above 60. The elderly.
