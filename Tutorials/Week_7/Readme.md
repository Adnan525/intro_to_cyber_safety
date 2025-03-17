# Introduction to Cyber Safety - Week 6: Email Safety and Security

## 1. How Email Systems Work

Email communication relies on several key components working together to deliver messages across the internet:

- **SMTP Servers (Simple Mail Transfer Protocol)**: The sender's email client connects to an SMTP server to convert and transmit email data.
- **DNS Servers**: When sending to different domains, the SMTP server queries DNS servers to locate the recipient's mail server.
- **POP3/IMAP Servers**: These manage how recipients access their emails:
  - POP3: Downloads only new emails received since the last check
  - IMAP: Creates a copy of emails that remain on the mail server, allowing access across multiple devices
- **Transmission Process**:
  1. Outgoing: Sender's device connects to SMTP server
  2. Redirect/Query: SMTP determines if recipient's domain is the same or different
  3. Exchange: Email transfers between servers
  4. Retrieve: Recipient accesses messages through email client using POP3 or IMAP

## 2. Email Security Measures

To ensure email security, implement these protective measures:

- **Account Separation**: Create separate email accounts for different purposes (work, financial transactions, social media)
- **Information Control**: Limit personal information in email addresses and signatures
- **Client Selection**: Choose email clients with strong security features (spam filtering, virus protection)
- **Content Protection**:
  - Block remote content that could contain tracking mechanisms
  - Disable message preview for suspicious emails
  - Check email headers to verify senders
- **Attachment Safety**: Never open attachments with .exe extensions or from unknown senders
- **Encryption**: Use email encryption when handling sensitive information:
  - S/MIME: Built into many devices (Apple, Microsoft)
  - PGP/MIME: Provides decentralized encryption options
- **Security Settings**:
  - Enable two-factor authentication
  - Regularly update passwords
  - Configure security settings for virus checking and spam filtering
  - Review connected apps and device access
- **Regular Maintenance**: Conduct security checkups and update email applications