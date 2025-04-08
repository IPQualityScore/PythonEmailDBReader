# IPQualityScore Email Validation & Verification Python DB Reader

## Flat File Version 1.0

Our flat file email validation database allows you to lookup important details about any email address using a straight forward library. Simply install the reader, download a database and instantly check email addresses against our large volume of data.

Click here to see the full [Python IPQualityScore flat file email validation database documentation](https://www.ipqualityscore.com/documentation/email-verification-database/python-database-reader). You may also find the information on our [email verification / email validation service](https://www.ipqualityscore.com/email-verification) helpful.

## Installation

You can easily install the Python database reader using pip:

pip install git+https://github.com/IPQualityScore/PythonIPQSEmailDBReader

## Usage

Using our flat file database system to lookup an email address is simple:

```
from util.emaillookup.emaillookup import EmailLookup
emailLookup = EmailLookup(path="path/to/bin")
results = lookup.lookupEmail("test@email.com")
print(results)
```

## Methods

Some of these fields may be unavailable depending on which database file you receive. If the field in question is unavailable in your database, the method will default to Pythons's default value for that type.

| Field | Type | Description |
|---|---|---|
| `record.valid()` | bool | Does this email address appear valid? |
| `record.disposable()` | bool | Is this email suspected of belonging to a temporary or disposable mail service? Usually associated with fraudsters and scammers. |
| `record.smtpScore()` | int | Validity score of email server's SMTP setup. Range: "0" to "3".<br><br>0x00 = mail server exists, but is rejecting all mail<br>0x01 = mail server exists, but is showing a temporary error<br>0x02 = mail server exists, but accepts all email<br>0x03 = mail server exists and has verified the email address |
| `record.suspect()` | bool | This value indicates if the mail server is currently replying with a temporary mail server error or if the email verification system is unable to verify the email address due to a broken SMTP handshake. This status will also be true for "catch all" email addresses. If this value is true, then we suspect the "valid" result may be tainted. |
| `record.catchAll()` | bool | Is this email likely to be a "catch all" where the mail server verifies all emails tested against it as valid? It is difficult to determine if the address is truly valid in these scenarios. |
| `record.deliverability()` | int | How likely is this email to be delivered to the user and land in their mailbox. Values can be "high", "medium", "low" or "none".<br><br>0x00 = none<br>0x01 = low<br>0x02 = medium<br>0x03 = high |
| `record.fraudScore()` | int | The overall Fraud Score of the user based on the email's reputation and recent behavior across the IPQS threat network. Fraud Scores >= 75 are suspicious, but not necessarily fraudulent. |
| `record.leaked()` | bool | Was this email address associated with a recent database leak from a third party? Leaked accounts pose a risk as they may have become compromised during a database breach. |
| `record.recentAbuse()` | bool | This value will indicate if there has been any recently verified abuse across our network for this email address. Abuse could be a confirmed chargeback, fake signup, compromised device, fake app install, or similar malicious behavior within the past few days. |
| `record.userVelocity()` | bool | Frequency at which this email address makes legitimate purchases, account registrations, and engages in legitimate user behavior online. Values can be "high", "medium", "low", or "none". Values of "high" or "medium" are strong signals of healthy usage. New email addresses without a history of legitimate behavior will have a value as "none". |
| `record.firstSeen()` | time.Time | When this email address was first seen online. |
| `record.domainAge()` | time.Time | Date when this domain was registered. |
| `record.domainCommon()` | bool | Is this email from common free email providers? ("gmail.com", "yahoo.com", "hotmail.com", etc.) |
| `record.domainVelocity()` | bool | Indicates the level of legitimate users interacting with the email address domain. Values can be "high", "medium", "low", or "none". This field is restricted to upgraded plans. |
| `record.domainDisposable()` | bool | Is this domain suspected of belonging to a temporary or disposable mail service? Usually associated with fraudsters and scammers. |
