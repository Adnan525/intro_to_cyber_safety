# Introduction to Cyber Safety - Week 3: Authentication/Passwords
## Question 1: Password System Security and Storage

### How Password Systems Work

Password systems operate as a fundamental authentication mechanism through a series of steps:

1. Account Creation
   - User selects a password during registration
   - System processes and securely stores the password
   - Additional security measures like email verification may be implemented

2. Authentication Process
   - User enters credentials during login
   - System validates entered password against stored version
   - Access granted only upon successful verification
   - May implement MFA(Multi factor authentication) or 3rd party authentication.

### Secure Storage Techniques

Modern password storage employs several critical security measures:

1. Cryptographic Hashing
   - Passwords are transformed into fixed-length hash values
   - One-way transformation prevents reverse engineering
   - Common algorithms: SHA-256, bcrypt, Argon2

2. Salting
   - Random data (salt) added before hashing
   - Unique salt per password
   - Prevents rainbow table attacks and identical password detection


## Question 2: Ensuring Password Strength and Preventing Reuse

### Technical Controls

1. Password Requirements
   - Minimum length: 12+ characters
   - Character complexity requirements
   - Entropy measurement
   - Real-time strength assessment

2. Anti-Reuse Measures
   - Password history enforcement
   - Hash comparison with previous passwords
   - Cross-platform credential checking
   - Integration with breach databases

### Policy and Education

1. User Training
   - Password creation guidelines
   - Security awareness programs
   - Phishing resistance training
   - Regular security updates

2. Administrative Controls
   - Regular password expiration policies
   - Account lockout procedures
   - Multi-factor authentication requirement

## Question 3: Future of Password Systems

### Current Limitations

1. Human Factors
   - Memory limitations
   - Password fatigue
   - Security vs. convenience trade-off
   - Tendency toward password reuse

2. Technical Constraints
   - Increasing computational power favors attackers
   - Database breach risks
   - Implementation complexities

### Future Evolution

Near-Term Developments
   - Passwordless authentication adoption
   - Pass key/API token
   - Biometric integration
   - Hardware security keys


## Hands-on Tasks

### W04T1: Password Generation Strategy

#### Strategy for Strong, Memorable Passwords

1. Base Phrase Method
   - Select meaningful phrase
   - Apply consistent transformation rules
   - Add personal elements

2. Example Implementation
   - Base phrase: "I enjoy learning!"
   - Transform: "iEnj0yLe4rn1ng"
   - Pattern: capitalize words, substitute numbers, add symbols

3. Strength Testing
   - Test using multiple password strength websites
   - Compare results across platforms
   - Analyze variation in scoring methods

### W04T2: Password Manager Comparison

#### LastPass Analysis

1. Strengths
   - Intuitive user interface
   - Cross-platform compatibility
   - Secure password sharing
   - Emergency access feature
   - Local encryption implementation

2. Weaknesses
   - Cloud storage dependency
   - Past security incidents (25th August, 2022)
   - Potential target for attacks

#### RoboForm Analysis

1. Strengths
   - Established reputation
   - Offline functionality
   - Advanced auto form filling
   - Business-oriented features
   - Application passwords support

2. Weaknesses
   - Limited sharing capabilities
   - Basic free version
   - Steeper learning curve
