
# Waste Management System Using AI

Welcome to our waste management system, a project aimed at promoting sustainable waste management practices using advanced AI and machine learning techniques. Our system is designed to help individuals and communities manage their waste in a more effective and efficient way, reducing environmental impact and promoting a healthier, more sustainable future.

Our waste management system uses Convolutional Neural Networks (CNN) to classify different types of waste materials, allowing users to easily identify and sort their waste into the appropriate categories for recycling and disposal. We have also integrated waste detection functionality, which can detect potential waste management issues or hazards, such as overflowing bins, litter, or illegal dumping.

In addition to waste classification and detection, our system also provides information on recycling methods for each type of waste, promoting environmentally responsible waste management practices. We have also included a notification system, which allows users to report waste issues to the appropriate authorities with just a few clicks.

## Problem Statement

Improper waste management not only poses a risk to human health and the environment but also represents a significant economic burden. The lack of effective waste classification and disposal methods has led to the accumulation of waste in landfills and oceans, causing pollution and resource depletion. To tackle these issues, we propose a waste management system that leverages AI-based waste classification and detection algorithms to optimize waste sorting and recycling, as well as provides users with recycling methods and educational resources. Our system aims to reduce waste generation, minimize contamination, and promote a circular economy that maximizes the value of waste materials.

## Tools and Technologies Used
- python
- OpenCV
- Tensorflow
- Convolutional Neural Network(CNN)
- Object Detection
- Streamlit
- pycharm(development)
- Google collaboratory(model training)


## Installation

### Install Python:
If you haven't already, you'll need to install Python on your local machine. You can download the latest version of Python from the official website: https://www.python.org/downloads/ and then follow the steps below

## Usage and features

- Waste classification: The system is be able to classify different types of waste materials using a convolutional neural network (CNN) algorithm. Users can upload an image of the waste material using the web interface, and the system should identify the material and display information on appropriate recycling methods.
- Waste detection: The system also includes waste detection capabilities using OpenCV or other computer vision libraries. This could involve identifying waste materials in real-time using a webcam or video stream.
- Recycling methods: Our system should provides information on appropriate recycling methods for each type of waste material. This could include information on recycling facilities or programs in the user's area, as well as guidelines for how to prepare the waste material for recycling.
- Waste Reporting: Our waste management system includes a notification system that allows users to report the presence of waste material to the relevant authorities. With just a few clicks, users can send an email to the authorities with an attached image of the waste material and location details. This feature helps to promote community involvement in waste management and encourages individuals to take responsibility for keeping their surroundings clean and hygienic. We believe that this feature can make a real difference in the fight against waste pollution and contribute towards building a more sustainable future.

## Screenshots and implementation
### First page
![Screenshot (69)](https://user-images.githubusercontent.com/66490787/230352785-1d7170bc-82bf-4417-9c8d-704ce90f711b.png)
### Second page
![Screenshot (70)](https://user-images.githubusercontent.com/66490787/230352803-db696d0f-fd9a-4dde-ad34-77980ef1ab5c.png)
### Third page
![Screenshot (71)](https://user-images.githubusercontent.com/66490787/230352815-c10f533a-a159-4333-b7ba-e2fad0d4a634.png)
### Fourth page
![Screenshot (73)](https://user-images.githubusercontent.com/66490787/230352831-200d8fb1-7e64-491b-8275-3919871cdf86.png)

## Run Locally

Clone the project

```bash
  git clone [https://link-to-project](https://github.com/sandy252/Waste-Management-System.git)
```

Go to the project directory

```bash
  cd Waste-Management-System
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run combined.py
```
Test the system: To test the waste management system, you can upload an image of waste material using the web interface. The system should classify the material using a CNN algorithm and display information on appropriate recycling methods.



## Future development
- Improved Waste Detection: One area for future development could be to improve the accuracy and efficiency of waste detection using advanced AI techniques such as deep learning and neural networks. This could involve training the system on a larger dataset of waste images, using more advanced CNN architectures, and incorporating real-time object recognition and tracking
- Mobile App Integration: Another area for future development could be to develop a mobile app that users can use to report waste material and receive notifications about waste management activities in their area. This could include features such as geolocation tracking, real-time updates, and social media integration.
- Waste Recycling: A third area for future development could be to provide more detailed information and guidance on recycling different types of waste material. This could include developing a database of recycling centers and facilities, providing tips on how to recycle different materials, and integrating a reward system to incentivize users to recycle more.
- Data Analytics: Finally, another area for future development could be to develop a more advanced data analytics platform that can provide insights into waste generation, disposal, and recycling patterns at the local, regional, and national levels. This could involve using big data analytics, machine learning, and data visualization techniques to identify trends and patterns, and inform waste management policies and strategies.

