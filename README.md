### Steps to Register a Domain Name at a DNS Registrar

1. **Choose a Domain Name**: Alice decides on the domain name `iot-techgagets.com`.

2. **Select a Domain Registrar**: Alice selects a domain registrar (e.g., GoDaddy, Namecheap) that is accredited to register domain names.

3. **Check Domain Availability**: Alice checks if `iot-techgagets.com` is available. If it is not already registered, she can proceed.

4. **Register the Domain**: Alice fills out the registration form, providing necessary information such as her name, address, and contact details. She also selects the registration period (usually 1 year or more).

5. **Payment**: Alice pays the registration fee to the registrar.

6. **Configure DNS Settings**: After registration, Alice can configure DNS settings, including setting up the authoritative DNS server (in this case, `dns.iot-techgagets.com`).

7. **Propagation**: Once registered, the information is propagated across the internet, which may take some time (usually up to 48 hours).

### DNS Resolution Process

When Bob wants to access `iot-techgagets.com`, his browser needs to resolve the domain name to an IP address. Here’s how the DNS resolution process works:

1. **Bob Enters the Domain**: Bob types `iot-techgagets.com` into his browser.

2. **Check Local Cache**: The browser first checks its local DNS cache to see if it has recently resolved this domain. If it finds the IP address, it uses that.

3. **Query the Recursive DNS Resolver**: If the IP address is not in the cache, the browser sends a DNS query to a recursive DNS resolver (usually provided by the ISP).

4. **Root DNS Server Query**: The recursive resolver checks its cache. If it doesn’t have the IP address, it queries a root DNS server. The root server responds with the address of the Top-Level Domain (TLD) server for `.com`.

5. **TLD Server Query**: The recursive resolver then queries the `.com` TLD server, which responds with the address of the authoritative DNS server for `iot-techgagets.com` (i.e., `dns.iot-techgagets.com`).

6. **Authoritative DNS Server Query**: The recursive resolver queries the authoritative DNS server (`dns.iot-techgagets.com`), which responds with the IP address associated with `iot-techgagets.com`.

7. **Return IP Address**: The recursive resolver caches the IP address for future requests and returns it to Bob's browser.

8. **Connect to the Server**: Bob's browser can now connect to the server at the resolved IP address to load the website.

### Diagram of DNS Resolution Process

```plaintext
Bob's Browser
     |
     | (1) Request iot-techgagets.com
     |
     v
Recursive DNS Resolver
     |
     | (2) Check local cache
     | (3) Query Root DNS Server
     |
     v
Root DNS Server
     |
     | (4) Respond with TLD Server for .com
     |
     v
Recursive DNS Resolver
     |
     | (5) Query .com TLD Server
     |
     v
.com TLD Server
     |
     | (6) Respond with authoritative DNS server for iot-techgagets.com
     |
     v
Recursive DNS Resolver
     |
     | (7) Query authoritative DNS server
     |
     v
dns.iot-techgagets.com (Authoritative DNS Server)
     |
     | (8) Respond with IP address
     |
     v
Recursive DNS Resolver
     |
     | (9) Return IP address to Bob's Browser
     |
     v
Bob's Browser
     |
     | (10) Connect to the server at the resolved IP address
     |
     v
Website Loaded
```

### Query Approach: Recursive vs. Iterative

- **Recursive Query**: In this approach, the DNS resolver takes on the responsibility of resolving the domain name completely. It queries other DNS servers on behalf of the client until it finds the answer. This is the approach used in the example above. It is preferred because it simplifies the process for the client (Bob's browser) and allows for better caching of results.

- **Iterative Query**: In this approach, the DNS resolver returns the best answer it has (which may not be the final answer) and the client must continue querying other servers. This is less common for end-user queries because it requires more effort from the client.

### Why Recursive Queries are Preferred

1. **Simplicity for Clients**: Clients do not need to manage multiple queries; they just send one request and receive the final answer.

2. **Efficiency**: Recursive resolvers can cache results, reducing the load on authoritative servers and speeding up future queries.

3
