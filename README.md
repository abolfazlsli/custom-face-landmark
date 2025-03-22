### **README for Face Landmark Detection Using OpenCV & Mediapipe**  

---

## **Introduction**  
This script uses **OpenCV** and **Mediapipe** to detect and visualize facial landmarks in real-time from a webcam feed.  

---

## **Requirements**  
### **1️⃣ Install Dependencies**  
Before running the script, install the required libraries:  

```bash
pip install opencv-python mediapipe
```

---

## **Usage**  
### **Run the script:**  
```bash
python face_mesh.py
```
📌 If you renamed the script, use the updated filename.  

### **Controls:**  
- Press **'Q'** to exit the program.  

---

## **How It Works**  
- Captures video from the webcam.  
- Detects **468 facial landmarks** using Mediapipe’s `FaceMesh`.  
- Draws **small circles** at each landmark position.  
- Converts frames between **BGR and RGB** for correct processing.  

---

## **Customization**  
- To **draw connections** between landmarks, uncomment this block in the script:  

```python
mp_drowing.draw_landmarks(
    image = img,
    landmark_list = face_landmark,
    connections = face_mp.FACEMESH_TESSELATION,
    landmark_drawing_spec = drawing_space,
    connection_drawing_spec = drawing_space
)
```

- To **label each landmark**, uncomment:  

```python
cv.putText(img, str(point), (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
```

---

## **Demo**  
<p align="center">
  ![Screenshot 2025-03-23 000634](https://github.com/user-attachments/assets/25898410-2439-4daa-a089-46c11d44abfb)
</p>  

---

## **License**  
This project is licensed under the **MIT License**.  

---

### **🚀 Happy Coding!**  
