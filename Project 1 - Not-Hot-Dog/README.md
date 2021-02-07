# Hotdog-OR-Not-Hotdog

[![](https://miro.medium.com/max/650/1*ubJ-RF8CKGvjckDEICsxsQ.png)](https://www.youtube.com/watch?v=pqTntG1RXSY&feature=youtu.be)

> "What would you say if I told you there is a app on the market that tell you if you have a hotdog or not a hotdog?"  -Jian-YangNot-Hot-Dog

This Repository has an implementation to Slicon Valley TV series scene about Jian-Yang's Hotdog/Not-Hotdog app.





### Tools
1. Keras Deep Learning Model.
2. Flask web service app.
3. Ionic Mobile app.




### How to use
Clone the repo via `git clone https://github.com/Jekso/Not-Hot-Dog.git` and follow those steps
1. Make sure you read Ionic documentation on how to setup enviroment from 'Getting Started' section from [here](https://ionicframework.com/docs).
2. Read Ionic documentation on how to setup enviorment for android from [here](https://ionicframework.com/docs/developing/android).
3. Install npm needed packages.
    - `npm install cordova-plugin-camera`
    - `npm install @ionic-native/camera`
    - `npm install cordova-plugin-advanced-http`
    - `npm install @ionic-native/http`
    - `ionic cap sync`
4. Install needed python libaries via `pip install -r requirements.txt`.
5. Download saved model and put it in 'model' folder from [here](https://drive.google.com/file/d/16VxJaUPupPzskCPzi-K2D9bsvffxPKsW/view?usp=sharing).
6. Run flask from 'web_service_app' folder via `python app.py` or upload app on [Heroku Cloud](https://www.heroku.com/).
7. If you run flask on your machine or uploaded it to Heroku make sure to update the host ip in 'ionic_mobile_app/src/app/home/home.page.ts' line 36, change `http://{ip address}:5000/predict`.
8. Build the app located in 'ionic_mobile_app' folder using capacitor via `ionic capacitor run android`.
9. When Android Studio opened just run the project and test it on your phone.
10. Always be happy cuz you only live once so go fkin nuts ^_^.




### Tutorial
pending...