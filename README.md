# Face-detection-and-glasses
A program that detects your face and draws glasses to them
![image0](https://github.com/user-attachments/assets/02521372-531a-47eb-837e-cb29071e2da8)



## About the project
I've always found interest and purpose in computer vision, how the computer "sees" objects or faces and recognizes them. Therefore, I have tried to combine my passion for criminalistics with previously mentioned field - computer vision and created a project on face detection. 


It's important not to confuse the term "Face detection" with "Face clustering", although the latter is more commonly used in forensics. Face clustering's purpose is to process multiple images of different faces and groups those that look alike. 
To further explain it, in a robbery case where the suspect would suddenly blend into the massive crowd in a public area, making it hard to spot him, face clustering could help us identify them even after a slight change in appearance, like beard or hairstyle, making it easier for law enforcement to find the culprit. 


#About the code
I used threading to execute 2 tasks simulataneously; by running the function "detection" in a seprate thread, the program doesn't stop or block but instead it continues displaying new video frames. Every 50 frames the function "detection" is performed, returning a boolean "face_match". Based on the result, the program either returns "MATCH!" or "NO MATCH!" and draws glasses on the person regardless of the final outcome. 


## Libraries used
- Opencv
- DeepFace
- Threading


