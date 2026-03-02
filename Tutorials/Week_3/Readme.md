# Introduction to Cyber Safety - Week 3: Internet Connectivity, Cookies, and Secure Communication

## 1. Devices We Use to Connect to the Internet

### Discussion Question
*What are the devices we use to connect to the internet?*

### Key Concepts

The range of devices capable of connecting to the internet has expanded enormously over the past two decades. These fall broadly into the following categories:

**Traditional computing devices** include desktop computers, laptops, and tablets — the devices most people associate with internet access.

**Mobile devices** such as smartphones are now the most common means of internet access worldwide, capable of connecting via both Wi-Fi and mobile data networks.

**Internet of Things (IoT) devices** represent a growing category of internet-connected hardware that extends well beyond screens. These include smart TVs, home assistants (such as Amazon Echo or Google Home), smart thermostats, security cameras, wearables (such as fitness trackers and smartwatches), and even appliances like fridges and washing machines.

**Networking equipment** such as routers and modems are themselves devices that connect to the internet and manage traffic between other devices and the broader network.

Understanding the full scope of connected devices in your environment is important for cyber safety, as each device represents a potential point of vulnerability.

---

## 2. Cookies: Types and Risks

### Discussion Question
*What are cookies? What types of cookies are used? Why should we be careful about cookie settings?*

### Key Concepts

**What are cookies?**

Cookies are small text files stored on a user's device by a web browser. They are used by websites to remember information about a user's visit — such as login status, preferences, or items in a shopping cart. Cookies are not programs and cannot execute code, but the data they store can have significant privacy implications.

**Types of cookies**

| Type | Description |
|---|---|
| **Session cookies** | Temporary cookies that exist only for the duration of a browser session. They are deleted when the browser is closed. Used for things like keeping a user logged in during a single visit. |
| **Persistent cookies** | Stored on the user's device for a set period of time, even after the browser is closed. Used to remember preferences or login details across multiple visits. |
| **First-party cookies** | Set by the website the user is currently visiting. Generally considered less intrusive, as they serve the functionality of that site directly. |
| **Third-party cookies** | Set by domains other than the one being visited — typically advertisers or analytics services. These are the primary mechanism behind cross-site tracking and targeted advertising. |
| **Secure cookies** | Only transmitted over encrypted (HTTPS) connections, reducing the risk of interception. |
| **HttpOnly cookies** | Inaccessible to JavaScript, providing some protection against cross-site scripting (XSS) attacks. |

**Why should we be careful?**

Third-party cookies in particular can build a detailed profile of a user's browsing habits across many websites, often without explicit consent. Most modern browsers offer options to block third-party cookies, and it is good practice to review and manage these settings regularly. Additionally, accepting all cookies on every website without consideration can expose users to unnecessary tracking.

---

## 3. Secure Communication on the Internet

### Discussion Question
*Which protocol should we use for secure communication on the internet? What are the ways we can ensure secured communication?*

### Key Concepts

**HTTPS**

The most widely used protocol for secure web communication is **HTTPS** (Hypertext Transfer Protocol Secure). It combines the standard HTTP protocol with **TLS** (Transport Layer Security) encryption, ensuring that data transmitted between a user's browser and a web server is encrypted and cannot easily be intercepted or tampered with.

Users can identify HTTPS connections by the padlock icon in their browser's address bar, and the URL beginning with `https://` rather than `http://`.

**SFTP**

For secure file transfer, **SFTP** (SSH File Transfer Protocol) is the recommended option. Unlike FTP, which transmits data in plain text, SFTP encrypts both commands and data, protecting against eavesdropping. It operates over SSH (Secure Shell) and is widely used in professional and enterprise environments.

Further reading: [ssh.com/ssh/sftp](https://www.ssh.com/ssh/sftp)

**Other methods for ensuring secure communication**

- **VPNs (Virtual Private Networks):** Encrypt internet traffic between a user's device and a VPN server, masking the user's IP address and protecting data on untrusted networks such as public Wi-Fi.
- **End-to-end encryption (E2EE):** Used in messaging applications (such as Signal or WhatsApp), ensures that only the sender and recipient can read messages — not even the service provider.
- **SSH (Secure Shell):** Used for secure remote access to servers and systems.
- **SSL/TLS certificates:** Issued by Certificate Authorities, these verify the identity of websites and enable encrypted connections.

---

## 4. Pop-ups: Positive and Negative Uses

### Discussion Question
*What are the positive and negative uses of pop-ups?*

### Key Concepts

Pop-ups are browser windows or overlays that appear automatically, either triggered by a website or, in malicious cases, by software on a user's device.

**Positive uses**

Pop-ups can serve legitimate purposes, particularly in marketing and user experience design:

- They can significantly increase conversion rates for newsletters, sign-ups, and promotional offers.
- They are effective at drawing attention to a single, focused call to action.
- They offer high return on investment for businesses due to their low implementation cost.
- Modern variants — such as slide-ins, banners, and exit-intent pop-ups — are designed to be less disruptive to the user experience.

**Negative uses and risks**

Pop-ups also carry real safety risks that users should be aware of:

- Malicious pop-ups may contain buttons labelled "Close" or "Cancel" that do not dismiss the window, but instead trigger further pop-ups or initiate a malware download.
- Some pop-ups originate not from websites but from **malware** that has been installed on the user's device without their knowledge.
- **Scareware** is a particularly harmful type of pop-up that falsely claims to have detected a virus, then attempts to sell fake security software — which may itself install further malware.
- Pop-ups can be used for **phishing**, directing users to fraudulent pages designed to steal credentials.

**Managing pop-ups safely**

To close a suspicious pop-up without clicking on it, use keyboard shortcuts such as `Ctrl + W` or `Alt + F4` on Windows. Most modern browsers include built-in pop-up blockers, which can be enabled in the browser's settings or content preferences.

---

## 5. Digital Device Inventory

### Discussion Question / Group Activity
*Assume you are required to take an inventory of the digital devices (computers, mobile phones, IoT devices, etc.) in your home or workplace for contingency planning. What attributes should the inventory list include?*

### Key Concepts

A **device inventory** is a fundamental component of both IT asset management and contingency planning. In the event of a security incident, disaster, or system failure, knowing exactly what devices exist, their configurations, and their roles allows for faster recovery.

**Suggested inventory attributes (titles only — do not share personal data with your group)**

- Device name / hostname
- Device type (laptop, smartphone, IoT sensor, router, etc.)
- Manufacturer and model
- Operating system and version
- MAC address
- IP address (static or DHCP-assigned)
- Location (room, floor, site)
- Owner / assigned user
- Purpose or role (e.g., work laptop, home security camera)
- Date of purchase / warranty expiry
- Software installed (key applications)
- Last security update / patch date
- Network it connects to (Wi-Fi SSID, wired LAN, etc.)

This activity highlights how many devices are often overlooked — particularly IoT devices — and why each one must be considered a potential security surface.

---

## Hands-On Tasks

### Task W03T1 — Managing Cookies and Pop-ups in Your Browser

**Objective:** Locate and adjust cookie and pop-up settings in your preferred browser.

**Steps (Google Chrome):**

1. Open Chrome and click the three-dot menu in the top-right corner.
2. Select **Settings** > **Privacy and security**.
3. Click **Cookies and other site data** to review and adjust cookie permissions (e.g., block third-party cookies).
4. Return to **Privacy and security** and click **Site settings** > **Pop-ups and redirects** to manage pop-up behaviour.

Other browsers such as Firefox, Edge, and Safari have similar settings accessible via their respective preferences or options menus. Refer to the lecture slides and tutorial recording for a guided walkthrough.

---

### Task W03T2 — Configuring a Router

**Objective:** Understand why routers are necessary and explore how to configure basic security settings.

**Why do we need a router?**

A router is the device that connects your local network (home or office devices) to the internet. It manages the flow of data between devices on your network and your Internet Service Provider (ISP). Without a router, devices cannot share an internet connection or communicate efficiently with one another on a local network.

**Key configuration steps (applicable to most popular routers):**

1. Access your router's admin panel by entering its IP address (commonly `192.168.0.1` or `192.168.1.1`) into your browser's address bar.
2. Log in with your admin credentials.
3. **Change the default admin password** — default passwords are publicly known and a significant security risk.
4. **Update the SSID** (the name of your Wi-Fi network) to something that does not identify you or your device model.
5. **Set the security mode** to WPA3 if supported, or WPA2 as a minimum. Avoid WEP, which is outdated and easily compromised.
6. Consider disabling remote management and WPS (Wi-Fi Protected Setup) if not needed.

Refer to the lecture slides and tutorial recording for a step-by-step demonstration.

---

*This document is intended for educational use. Please refer to your unit outline for assessment requirements and submission guidelines.*