#  Face Recognition – Ethiopian Icons 🇪🇹

This project is part of my **6-month learning journey** to become a Computer Vision Specialist.  
It uses OpenCV to recognize 3 well-known Ethiopians.

## 👩‍💻 Recognized People
- Haile Selassie
- Meles Zenawi (a bit tricky due to glasses)
- Liya Kebede

## ⚙️ Technologies
- Python
- OpenCV
- Haarcascade (face detection)
- LBPHFaceRecognizer (face recognition)

## 💡 What I Learned
- Face detection with Haar cascades
- Preprocessing images: converting to grayscale
- Training and predicting faces using OpenCV
- Drawing bounding boxes and adding labels

---

## 📸 Demo Outputs

<table>
  <tr>
    <th>🔍 Input Image</th>
    <th>✅ Recognition Result</th>
  </tr>
  <tr>
    <td><img src="./imagesForDescription/original.png" width="200"/></td>
    <td><img src="./imagesForDescription/detected.png" width="200"/></td>
  </tr>
  <tr>
    <td><img src="./imagesForDescription/haileOriginal.png" width="200"/></td>
    <td><img src="./imagesForDescription/hailePredicted.png" width="200"/></td>
  </tr>
  <tr>
    <td><img src="./imagesForDescription/melesOriginal.png" width="200"/></td>
    <td><img src="./imagesForDescription/melesPredicted.png" width="200"/></td>
  </tr>
</table>

> All demo images are located in the `/imagesForDescription` folder.

---

## 🧪 How to Run

```bash
pip install opencv-python
python Face_recognition.py
