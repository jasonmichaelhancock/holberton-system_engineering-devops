0x19-postmortem

Summary: On September 21, 2018, starting at 6:30pm PDT CherubFish experienced a major DDoS attack which caused our service to go offline for nearly 24 hours. The attack saw internet traffic of up to 5gb/s which is twice our capacity shortly after launch. 100% of users experienced hangtime that resulted in almost all users exiting the application. The attack began at a moment the entire company was attending a Grand Opening party and as such the system was left unobserved for most of the evening.

Timeline:

September 21, 2018

6:30pm PST: Entire CherubFish Team leaves CherubFish premises to attend Grand Opening gala.
6:37pm PDT: CherubFish server traffic increases by double in one minute.
8:15pm PDT: Cherubfish server traffic exceeds capacity of servers for zero reduction in service.
8:87pm PDT: Cherubfish server traffic reaches level to effectively render site down.
September 22, 2018

8:30am PDT: CherubFish Marketing Director notices that site is down, activates CherubFish phone tree.
9:30am PDT: CherubFish emergency team meeting convened.
11:07am PDT: CherubFish DDoS response plan put into motion.
4:45pm PDT: Web server traffic returns to normal state.
Root Causes and Resolution:

CherubFish had put into place a DDoS device capable of handling a 5gb/s event, which had never been put to use in a real event. While the DDoS attack remained below 5gb/s the attack did cause a slowdown of our site but after the DDoS attack exceeded 5gb/s it caused slowdown to the extent that for almost all users the response delay resulted in user navigating away from page. Once CherubFish Marketing director Amy Galles noticed the outage an emergency meeting was convened of all CherubFish staff.
One team worked to see if they could obtain and bring online another 2 DDoS devices but that effort ultimately failed within the given timeframe as it was the weekend and the supplier was not available.
Another Team set out to alter the system to fight the attack through the following measures: lower the timeout limit for open connections, set lower SYN, ICMP, and UDP flood drop thresholds, drop spoofed or malformed packages. These measures were effective and remain in effect even now.
Next we contacted our Internet Service provider and informed them of the attack. They black-holed the site for a short time, and brought the site back on line using a data scrubber than was able to analyze the packets stream comparing it to that before the DDoS attack and remove suspicious packets. This resulted in a steady reduction in server traffic and ultimately a return to regular service. In its report to CherubFish JoeBlow Hosting, Inc identified Jawfish, a competing Holberton School startup, as the source of the DDoS attack.

Corrective and Preventative Measures:

Create a DDoS Playbook: As a new team we were unprepared for this attack. The first an most obvious corrective is that we must build into our system a more robust monitoring and notifying system than what we had in place, which was one employee noticed the site is down. If the whole team is at a party we must have at least one person on-call 247 to monitor notifications in real time.

The playbook would also have a sequence of steps that would be undertaken immediately upon notification of an attack. The plan will have all info needed to fight the attack and especially given the resolution of this attack a close working relationship with our ISP.

We also need to put into place a section of the playbook that deals more effectively with communicating the outage and efforts to correct to end users.

It is also recommended that the company consider hiring a DDoS mitigation specialist by weighing the cost against the likelihood of future attacks and the effect on the business of such attacks.

The company will also put in place additional DDoS devices to handle smaller attacks.