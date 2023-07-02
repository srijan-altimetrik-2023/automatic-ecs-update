terraform {
backend "s3" {
    bucket     = "ami-automate-s3"
    key        = "state.txt"
    region = "ap-south-1"
  }

}
provider "aws" {
  region = "ap-south-1"
  access_key = "ASIASYQ3HBXP26YBTFVU"
  secret_key = "ASIASYQ3HBXP26YBTFVU"
  token = "IQoJb3JpZ2luX2VjEGwaCXVzLWVhc3QtMSJGMEQCICfMErfvld5tcQst+rp98VtHxWW6RKNnHfbqyNuvrTFjAiABOLeOEPsRg0GwzZhnTPGBzLs1dzDSjjd8QPxMNW19TCqgAwjV//////////8BEAAaDDE5MDEwOTM4ODI1NSIM4t2kGT4S2b6eDgv6KvQCUu2nShJVOwldsq9D3duazH5yjE+Yg7yTUntt9x8lukNuvLThgdJq/rduajhUc6Ic3s8xRjz2EVh3o6sVaKrQPT9YEUp1TBqMTv2secBSBUXofB8Ln9pcNYahghLyqQol2CnQ6FazrcarGLtvUiIXjpBd3PUZdk4SFXLDN2GyQzbH7gq6eWggYFH+Y8AORQsBkmBqmKzE34VFojbXQ/NqBeC+gYLMWOMRnqFboPXptir7fFFEreUk5k4ZOQUpyRPPWoc0COZRKY5kGcob5gzWCDeskp1Vo6IoYyrkjStFZPKJbnj/CBkSZP8vlTjfehKv4W2n+C07UyVE6Nz6NKoA0kMuPac9ijHMh2uvn60APMD7u90fou7BtiB8/3lfXBNXKaoQi4/DFCLyccpX1juKI1+woRgKp/VCknvaZRTUC1f3d5LV/iU9Q1Z9z/QQK4pgfoUI6bUNo7ANEBP9mnSDQCEU91wlEZ0Skd8tKLsa1jTC71yGMPa9haUGOqcBSvQ0EVR/Hmkf933TGUA7ceVNcgoxjWPlcsgjRFJnODJnSQM00ZIt5FjNp144hTkpdDXqyJ/UPupB79szOONk5L3RHquMNC5/xHDvXhROBoJSBQTG30gsFxOuCi/2J5Ws2LOaXiPbtFxFMPi7uBli4d0JyfaLiyGyeBPHfCZBLWcBIVNAevJr+YgikAj98X3H0qqmbAHe46I8L2N76odIXLdVC4IDaV4="

  default_tags {
    tags = {
      Environment = "Prod"
      Application = "Testing"
      Project = "CloudOps"
      Owner = "mnageti@altimetrik.com"
    }
  }
}
