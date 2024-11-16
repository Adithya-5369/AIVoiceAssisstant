**AIVoiceAssistant**

**A Multi-Functional Voice-Controlled AI Assistant in Python**

---

**Overview**

AIVoiceAssistant is an all-in-one Python-based AI assistant designed to enhance productivity and convenience through voice commands. With capabilities ranging from opening applications to searching the web, sending emails, playing music, and managing tasks, this assistant offers seamless interaction via speech recognition and synthesis.

The assistant also includes a built-in dictionary, Chrome automation features, and smart handling of application paths and configurations, all within a single Python script.

---

**Features**

- **Voice Interaction:**
  - Convert speech to text for interpreting user commands.
  - Text-to-speech responses for better user interaction.
  
- **Application Management:**
  - Open frequently used applications such as Chrome, Notepad, VLC Media Player, and more.

- **Web Searches:**
  - Perform Google and YouTube searches.
  - Retrieve information from Wikipedia.

- **Email Functionality:**
  - Send emails directly by providing the recipient's address and content through voice.

- **Music Playback:**
  - Automatically play music from a specified directory.

- **Dictionary Integration:**
  - Get meanings, synonyms, and antonyms for words.

- **Customizable Configuration:**
  - Add or update paths for applications and music directories in the script.
  - Embedded email credentials for seamless email handling.

- **Additional Functionalities:**
  - Get the current time.
  - Execute system commands like shutdown or restart.
  - Chrome automation for tab and window management.

---

**How to Use**

1. **Install Prerequisites:**
   Ensure Python 3.x is installed and the following libraries are installed:
   ```bash
   pip install pyttsx3 speechrecognition wikipedia PyDictionary
   ```

2. **Configuration:**
   - Update the `CONFIG` dictionary in the script with:
     - Paths to applications (e.g., VLC, Chrome, etc.).
     - Email credentials for sending emails.
     - Directory path for music playback.

3. **Run the Assistant:**
   Execute the script:
   ```bash
   python AIVoiceAssistant.py
   ```

4. **Give Commands:**
   - Example voice commands:
     - "Open Notepad"
     - "Search Wikipedia for Python"
     - "Send email to xyz@example.com"
     - "Play music"

---

**Requirements**

- **Python 3.x:** For running the script.
- **Libraries:**
  - `pyttsx3` for text-to-speech functionality.
  - `speechrecognition` for voice recognition.
  - `wikipedia` for fetching summaries.
  - `PyDictionary` for word definitions.
- **Internet Connection:** Required for web searches and email functionalities.

---

**How It Works**

1. **Speech Recognition:**
   - Listens to user commands via a microphone.
   - Converts speech to text using Google Speech Recognition.

2. **Task Execution:**
   - Processes commands to identify tasks.
   - Executes tasks like opening apps, sending emails, or performing searches.

3. **Responses:**
   - Uses text-to-speech to provide feedback or results to the user.

4. **Dynamic Configurations:**
   - Paths for apps, music directories, and email credentials are embedded for easy customization.

---

**Additional Notes**

- Ensure microphone access for voice commands.
- Configure paths and email credentials securely before use.
- The assistant uses Python libraries and may require permissions for system-level commands.

---

**About**

- **Developer:** Adithya Sai Srinivas  
- **Purpose:** To create a smart, universal assistant for simplifying everyday tasks with a focus on user interaction and convenience.

---

**Resources**

- **Languages:** Python (100%)
- **Documentation:** Detailed in-script comments for easier understanding.
- **Platform:** Compatible with Windows, macOS, and Linux.

---

**Suggested Workflows**

1. **Python Package Testing:**
   - Create and test Python functionality across multiple environments.

2. **Application Automation:**
   - Build on this project to include additional commands or integrate with APIs.

---

Enjoy seamless interaction with your **AIVoiceAssistant** today!
