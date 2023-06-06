## FUNCTIONAL PROCESS FLOW (USER-SIDE)

The objective of specifying this flow is to provide users with a clear understanding of how to effectively use the smart light bulb application and its associated features. The use-case outlines steps undertaken by users for seamlessly integrating their smart light bulbs into their homes, controlling them remotely, and personalising their settings. It takes only prototype-level model implementation and focuses on how the basic functionalities would ensue. Additionally, the objective is to ensure that users can easily share access with others, enabling a collaborative and connected experience for multiple users within a household or shared space.

Actors:

1. Primary User - The primary user who owns and controls the smart light bulbs.
2. Shared Users - Other users with whom the primary user shares access to the light bulbs.

Preconditions:

1. The smart light bulbs are installed and connected to the user's home network.
2. The user and shared users have installed the smart light bulb application on their respective devices.

Flow of Events:

1. User Registration and Login:
   a. The user downloads and installs the smart light bulb application on their device.
   b. The user opens the application and registers a new account or logs in using existing credentials through either standard google-based login.

2. Adding Device:
   a. After logging in, the user navigates to the "Add Device" section within the application.
   b. The user enters the lightbulb code or scans the QR to add the device (Assumption: Set-up codes available on devices) which connects the application through bluetooth or WiFi based pairing.
   c. The user then saves the device, and the smart light bulb is added as one of the devices being automated using the account.

3. Controlling Light Bulbs:
   a. On the application's home screen, the user can see a list of their connected light bulbs.
   b. The user selects a specific light bulb to control.
   c. The user can turn the light bulb on or off by using the physical button on the light bulb or by tapping the corresponding button in the application.
   d. When the light bulb state changes, the application receives a notification and updates the status accordingly.

4. Managing Light Bulb Settings:
   a. The user can access and modify the settings of each light bulb by selecting it from the application's "Your devices" section.
   b. The user can change the light bulb's name, color, brightness, on time, and off time.
   c. The modified settings are sent to the light bulb, and the application updates the displayed information.

5. Sharing Light Bulbs:
   a. The user can choose to share access to a specific light bulb with other users.
   b. The user navigates to the "Share access" section within the application.
   c. The user enters the name and email addresses or usernames of the shared users.
   d. The shared users receive an invitation to access the light bulb and can control it through their own installed smart light bulb application.

6. Adaptable Application:
   a. The smart light bulb application is developed as a hybrid application to ensure compatibility across various platforms, including iOS, Android, and web.
   b. Users can download and install the application from their respective app stores or access it through a web browser.

Postconditions:

1. The user and shared users can control their connected smart light bulbs through the application, adjusting their settings, turning them on or off, and scheduling their operation.
2. The hybrid application provides a consistent user experience on different platforms, ensuring accessibility and convenience.

Alternative Flows (Addressing potential break-points):

1. If there is a connectivity issue between the smart light bulbs and the user's home network, the application displays a message indicating the inability to connect and prompts the user to check their network settings or contact support.
2. If a shared user is removed from the access list by the primary user, their access to the shared light bulb is revoked, and they no longer have control over it.
3. If there are multiple users trying to control the same light bulb simultaneously, the application should prioritise the most recent command to avoid conflicts or confusion.
