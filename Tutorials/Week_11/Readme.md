# Introduction to Cyber Safety - Week 11: Beyond technology—dealing with people

## Report on Social Media Data Breaches and Protective Measures
1. Steps to Determine if Your Account Information Has Been Breached
When major data breaches occur like those affecting Facebook and LinkedIn, individuals can take specific steps to determine if their information has been compromised:
- Check dedicated breach notification services: Websites such as HaveIBeenPwned.com allow users to enter their email addresses or phone numbers to check if they appear in known data breaches. This service maintains a comprehensive database of compromised accounts across multiple platforms and notifies users if their information appears in new breaches.
- Monitor official communications: Companies typically notify affected users directly after confirming a breach. Check your email (including spam folders) for notifications from the platform about security incidents. Both Facebook and LinkedIn sent notifications to affected users following their respective breaches.
- Check account activity logs: Most social media platforms maintain activity logs that show login locations, devices, and timestamps. Unusual activity such as logins from unfamiliar locations or devices may indicate unauthorized access. On Facebook, this can be found under "Security and Login" in settings, while LinkedIn offers "Where You're Signed In" under the security section.
- Use platform-specific tools: Facebook's "Security Checkup" tool and LinkedIn's "Account Security" section offer ways to review recent account activity and security status. Facebook specifically created a tool after its breach allowing users to check if their phone numbers were among those exposed.
- Watch for signs of compromise: Unexpected password reset emails, posts you didn't create, messages sent without your knowledge, or contacts receiving suspicious messages from your account may indicate a breach.


2. Measures to Protect Accounts in the Future
After confirming whether your accounts were compromised, implementing these protective measures can enhance security:
- Implement strong, unique passwords: Create complex passwords of at least 12 characters including a mix of uppercase, lowercase, numbers, and special characters. Most importantly, use different passwords for each online account to prevent credential stuffing attacks.
- Enable two-factor authentication (2FA): Both Facebook and LinkedIn offer 2FA options that require a second verification step beyond password entry. This typically involves receiving a code via SMS, using an authentication app, or employing a physical security key.
- Regularly update personal information: Limit the personal information shared on your profile. Periodically review privacy settings and remove unnecessary personal details, work history, contact information, or other sensitive data that could be exploited if leaked.
- Monitor third-party access: Review and revoke access for unnecessary third-party applications or services connected to your social media accounts. These connections can become security vulnerabilities if the third-party service experiences a breach.
- Keep software updated: Ensure your devices, browsers, and apps remain updated with the latest security patches. Outdated software often contains vulnerabilities that hackers can exploit.
- Be vigilant about phishing attempts: Exercise caution with unexpected messages, especially those requesting personal information or containing suspicious links. Data breaches often lead to increased phishing attempts targeting affected users.
- Consider using a password manager: Services like LastPass, 1Password, or Bitwarden can generate and store strong, unique passwords for all your accounts, reducing the risk from password reuse.


3. Comparing the Facebook and LinkedIn Data Breaches

**Similarities**
- Scale of impact: Both breaches affected massive user bases – approximately 533 million Facebook users and over 500 million LinkedIn users.
- Type of data exposed: Both leaks exposed personally identifiable information (PII) including names, email addresses, phone numbers, employment information, and location data.
- Method of exploitation: Both breaches involved scraping data rather than direct database hacks. Attackers exploited features and APIs designed for legitimate use to collect information at scale.
- Delayed discovery and disclosure: In both cases, the companies discovered the full extent of the breaches only after data was already circulating among hackers, indicating insufficient monitoring systems.
- Monetization by attackers: The stolen data from both platforms was packaged and sold or shared on hacking forums, creating lasting privacy concerns for affected users.

**Differences**
- *Facebook breach specifics:* The Facebook breach primarily stemmed from a vulnerability in the platform's contact importer feature before 2019. The data was initially sold on dark web forums before being leaked publicly for free in 2021. Facebook claimed the vulnerability had been patched in 2019, making this "old data."
*LinkedIn breach specifics:* The LinkedIn breach involved data scraping that exploited the platform's API. The company maintained that no private member account data was compromised, characterizing the incident as "aggregation of data from LinkedIn and other websites," rather than a data breach in the traditional sense.
- Company response: Facebook was criticized for not notifying affected users individually, while LinkedIn was somewhat more proactive in its communication, though both faced criticism for downplaying the seriousness of the incidents.
- Regulatory consequences: Facebook faced more significant regulatory scrutiny following its breach, particularly from EU regulators under GDPR, while LinkedIn faced comparatively less regulatory pressure.

Recommendations
- For Platform Companies
    - Implement more robust rate limiting: Both Facebook and LinkedIn could have better detected and prevented mass data scraping by implementing stricter API rate limits and monitoring unusual data access patterns.
    - Conduct regular security audits: More frequent and thorough security assessments could have identified the vulnerabilities before they were exploited at scale.
    - Improve data minimization practices: Platforms should collect and retain only necessary user information, reducing potential exposure during breaches.
    - Enhance breach notification protocols: Both companies should develop more transparent and timely notification systems to alert users immediately when their data has been compromised.
    - Provide better user education: Platforms should more actively educate users about privacy settings, potential risks, and security best practices when using their services.
- For Individual Users
    - Practice data minimization: Share only essential information on social platforms; leave optional profile fields blank, especially for sensitive information.
    - Regularly review privacy settings: Schedule quarterly reviews of privacy and security settings on all active social media accounts.
    - Create separate email addresses: Use different email addresses for critical services versus social media to minimize crossover risks from breaches.
    - Be skeptical of connection requests: Verify unexpected connection requests, as scraped data enables more convincing targeted social engineering attacks.
    - Consider digital footprint implications: Remember that information shared online can potentially become permanent and public, regardless of platform privacy promises.