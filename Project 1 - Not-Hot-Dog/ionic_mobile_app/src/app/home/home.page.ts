import { Component } from '@angular/core';
import { Camera,  CameraOptions} from '@ionic-native/camera/ngx';
import { HTTP } from '@ionic-native/http/ngx';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage
{
  
  url = 'https://not-hot-dog.herokuapp.com/predict'
  
  prediction_image = '';
  placeholder_image = '../../assets/image_placeholder.png';
  is_loading = false;
  is_predicted = false;

  constructor(private http: HTTP, private camera: Camera)
  {

  }



  take_photo()
  {
    const options: CameraOptions = {
      quality: 90,
      destinationType: this.camera.DestinationType.DATA_URL,
      encodingType: this.camera.EncodingType.JPEG,
      mediaType: this.camera.MediaType.PICTURE,
      targetHeight: 200,
    }

    this.camera.getPicture(options).then((imageData) => {
      this.is_loading = true;
      this.is_predicted = false;
      this.placeholder_image = 'data:image/jpeg;base64,' + imageData;
      this.http.setDataSerializer('json');
      this.http.post(this.url, {image: imageData}, {})
          .then(data => {

            data.data = JSON.parse(data.data);
            this.is_loading = false;
            if(data.data.prediction == 'hotdog')
            {
              this.prediction_image = '../../assets/hot_dog.png';
            }
            else
            {
              this.prediction_image = '../../assets/not_hot_dog.png';
            }
            this.is_predicted = true;

          })
          .catch(error => {
            console.log(error.error);
          });

     }, (err) => {
        console.log(err);
     });
  }

}
