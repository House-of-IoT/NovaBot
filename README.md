# NovaBot

## What is the nova bot?
Nova is meant to be a beginner IoT project for PBL. Not only does Nova act as PBL , it provides actual functionality that you could use to improve your workflow hands-free.

## General
Nova is a general purpose assistant that has the following functionality:

- Speech Recognition to interact with many different apis(Requires you to physically be with the device)
  - your surrounding Weather
  - your personal github
  - geek quotes
  - geek jokes
  - gather your connected server's status(other connected nova bots)

- Cloud connectivity
  - Nova connects to the [Nova-Remote-Server](https://github.com/House-of-IoT/Nova-remote-server) which can dictate the actions and availablity of the device. The remote server is treated as the "final decision" to the device(keep in mind you don't have to connect to the remote server for speech recognition to work)
  
- Streaming 
   - Nova has a camera that is used to stream video to the [Web-Client](https://github.com/House-of-IoT/HOI-WebClient) 
   - Nova has a microphone that is used to stream audio to the [Web-Client](https://github.com/House-of-IoT/HOI-WebClient)
   
- Alarm Mode
   - Nova has alarm mode(that you have to enable) that is utilizes the camera and the passive infared sensor to create push  security alert notifications to your remote server.
   - Nova's alarm mode is fully customizable with time intervals and recording intervals.
  
- Ease of setup
  - Nova's physical devices and software setup is designed to be as simple as possible for any beginner. The physical devices require NO SODERING(which is true for majority of the HOI projects) , for this project we are using female to female dupont wires which are plug and play.



SETUP WIKI COMING SOON ONCE FINALIZED.
