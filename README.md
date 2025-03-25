# my_cartoon_rendering

해당 프로젝트는 Opencv를 활용한 간단하게 카툰 렌더링을 할 수 있는 Python 프로그램입니다.


## 나의 알고리즘으로 만화 같은 느낌이 잘 표현되는 이미지 데모

 ![Image](https://github.com/user-attachments/assets/989bed4f-e6d8-46ee-b85f-4a05c60ea462)

![Image](https://github.com/user-attachments/assets/67a5794f-384f-47ea-94a1-9d0b69ac6b9b)

선명한 배경과 단순한 색상을 가진 이미지, 윤곽선이 명확하고 대비가 큰 이미지, 사람 얼굴이나 동물 이미지에서 단순화된 색상과 구분이 확실한 형태를 가진 이미지의 경우 밝고 뚜렷한 윤곽선이 이미지의 특징을 강조하고, 전체적인 색상이 균일하게 변하면서 만화 스타일을 잘 표현합니다.

## 나의 알고리즘으로 만화 같은 느낌이 잘 표현되지 않는 이미지 데모
  
 ![Image](https://github.com/user-attachments/assets/3e38ca91-a77f-4dc0-a7b0-4a6b45e1a1b2)

 ![Image](https://github.com/user-attachments/assets/b5080a2f-bb79-434f-b87e-7ee9c2d72919)

매우 복잡한 배경을 가진 이미지, 세밀한 디테일이나 다양한 색조를 가진 이미지, 너무 많은 텍스처가 있는 이미지의 경우 복잡한 디테일을 단순화하려고 하면 이미지가 부자연스럽게 변하고, 텍스처가 너무 많이 사라지거나 왜곡되는 경우가 많습니다.

## 나의 알고리즘의 한계점

1. 복잡한 배경에서의 문제 : 이미지의 배경이 복잡하거나 텍스처가 많으면 색상 단순화가 잘 되지 않고 만화 스타일이 어색하게 표현됩니다. 배경과 객체를 구분하기 어려워 만화 느낌을 제대로 살리기 어렵습니다.

2. 세밀한 디테일 손실 : 원본 이미지에서 세밀한 디테일이나 텍스처가 중요한 경우에 색상 단순화나 모서리 부분의 강조 과정에서 중요한 세부사항이 손실될 수 있습니다.

3. 색상 왜곡 : 프로그램이 색상을 단순화하는 과정에서 원본 색상에서 벗어날 수 있습니다. 이로 인해 실제 이미지의 색상이 왜곡될 수 있으며 이미지의 자연스러움이 감소할 수 있습니다.

4. 고정된 필터에 의존: cv2.pyrMeanShiftFiltering()이나 cv2.adaptiveThreshold()와 같은 고정된 필터에 의존하기 때문에, 다양한 스타일이나 세밀한 조정을 통해 만화 스타일을 다채롭게 변형하는 데 한계가 있습니다. 보다 창의적이고 다양한 만화 스타일을 구현하기 위해서는 이에 대응하는 다양한 필터 및 코드가 필요합니다.
