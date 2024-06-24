# Postmortem: Web Application Outage on July 14, 2023

## Issue Summary

**Duration:** July 14, 2023, 10:00 AM - 12:30 PM GMT

**Impact:** The main web application was down for 2 hours and 30 minutes. Users experienced a complete inability to access the website, resulting in a 100% outage for all users. Approximately 10,000 users were affected during this period, impacting our daily active user base significantly.

**Root Cause:** The root cause was a misconfiguration in the Nginx load balancer, which failed to route traffic to the backend servers due to an expired SSL certificate.

## Timeline

- **10:00 AM GMT** - Issue detected via automated monitoring alert from New Relic indicating a sharp drop in web traffic and server errors.
- **10:05 AM GMT** - On-call engineer confirmed the outage and began initial diagnostics.
- **10:10 AM GMT** - Verified that the web servers were operational but not receiving traffic from the load balancer.
- **10:15 AM GMT** - Assumed the issue was related to a recent deployment and started rolling back changes.
- **10:30 AM GMT** - Rolled back the deployment, but the issue persisted.
- **10:45 AM GMT** - Escalated to the senior DevOps team for deeper investigation.
- **11:00 AM GMT** - DevOps team identified that the Nginx load balancer was not forwarding requests to the backend servers.
- **11:15 AM GMT** - Investigated the Nginx configuration and logs, discovered SSL certificate had expired.
- **11:30 AM GMT** - Began the process to renew and update the SSL certificate.
- **12:00 PM GMT** - SSL certificate was renewed and updated in the Nginx configuration.
- **12:15 PM GMT** - Restarted Nginx service, verified that traffic was now being correctly routed.
- **12:30 PM GMT** - Full service restored, and all systems operational.

## Root Cause and Resolution

**Root Cause:**
The root cause of the outage was an expired SSL certificate on the Nginx load balancer. The certificate expired at 10:00 AM GMT, which caused Nginx to stop routing traffic to the backend servers, leading to a complete outage of the web application.

**Resolution:**
The issue was resolved by renewing the SSL certificate and updating the Nginx configuration to use the new certificate. The steps included:
1. Identifying the expired SSL certificate through Nginx logs and configuration files.
2. Generating a new SSL certificate using Certbot.
3. Updating the Nginx configuration file to include the path to the new SSL certificate.
4. Restarting the Nginx service to apply the changes and verify that the load balancer was correctly routing traffic to the backend servers.

## Corrective and Preventative Measures

**Improvements/Fixes:**
1. **Automate SSL Renewal:** Implement automated SSL certificate renewal using Certbot's auto-renew feature to prevent future certificate expiration issues.
2. **Enhanced Monitoring:** Set up alerts specifically for SSL certificate expiration dates.
3. **Documentation:** Update documentation to include steps for manual SSL certificate renewal and verification.
4. **Testing:** Include SSL certificate checks in the deployment pipeline to catch issues before they reach production.

**TODO Tasks:**
1. **Patch Nginx Server:**
   - Configure Certbot for automated SSL renewal.
   - Test and verify automated renewal process.
2. **Add Monitoring:**
   - Implement SSL certificate expiration alerts in New Relic.
   - Verify alerts are triggered well before expiration (e.g., 30 days in advance).
3. **Update Documentation:**
   - Document SSL certificate renewal procedures.
   - Include troubleshooting steps for SSL-related issues.
4. **Enhance Deployment Pipeline:**
   - Add SSL checks to CI/CD pipeline.
   - Ensure that any changes to SSL configurations are tested in staging before production.

By addressing these measures, we aim to prevent similar incidents in the future and ensure higher reliability and availability of our web services.
