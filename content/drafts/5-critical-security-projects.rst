5 critically important security projects
========================================

Information security is hard. Really hard. But all too often the face of our
failure is not cutting edge research with intricate implementation, but rather
trivial buffer overflows, databases with plaintext passwords, or binaries named
``tacos_and_malware.exe``.

'tis a bleak and barren landscape of horrors and awful things untold.

That said, amidst our dystopian present, there are a few critically important
projects doing great work to push the needle forward on security, and I'd like
a moment in this festive Thanksgiving season to recognize their outstanding
work:

* **u2f**: Universal second factor. This is a standard for hardware devices
  which provide a "second factor" for logging into websites, replacing
  "Google Authenticator" on your phone. The thing that makes *u2f* really
  outstanding is that not only does it protect against password theft, but also
  protects against phishing. Phishing is one of the most pernicious attack
  vectors, as it's demonstrably impossible (to say nothing of fundamentally
  unreasonable) to ask people to stop clicking links in their email. A widely
  deployed cryptographic solution to phishing would be a tremendous victory.
  *u2f* devices are currently available for sale.
* **letsencrypt**: Lets Encrypt is a new certificate authority launching in
  just a week. It will provide free certificates to website operators, as well
  as an API and tooling for *automatic* certificate provisioning. The price
  point and the automation will be a huge help to getting more websites
  deployed with HTTPS, bringing us to a world where MITM-free is the default
  for web browsing, not the special privilege of banks.
* **Rust**: Rust is a new programming language, whose development is being
  funded by Mozilla. Rust is important because it combines the low-levelness
  and performance of *C* with the safety of a higher-level language. A ton of
  software vulnerabilities are still caused by memory-unsafety and Rust goes a
  long way to obliterating those. Rust's 1.0 release was earlier this year.
* **X25519/Ed25519**: *X25519* is an elliptic curve key exchange algorithm, and
  *Ed25519* is an elliptic curve signature algorithm. They are important for
  two reasons: a) they remove concerns that some have about the current crop of
  elliptic curves (notably P-256) having some sort of NSA backdoor, and b)
  they are easier to implement correctly and provide increased resistance
  against all manner of side channel attacks. Uptake of elliptic curve
  cryptography is important because algorithms such as RSA are proving weaker
  than we expected, due to advances in "index calculus". They are currently
  working their way through IETF standardization and will hopefully find their
  way into a TLS stack near you shortly.
* **Chromebook**: It's the holiday season, which means I just spent an hour
  de-malwaring my family's computers. Chromebooks bring to the desktop much
  needed sandboxing, preventing malicious content for taking over things like
  your bank's website. Chromebooks achieve this by moving everything to run
  under the web's security model, whereas *iOS* achieved similar ends using
  native sandboxing. Chromebooks are available for sale now.
