```mermaid
gantt
        dateFormat  YYYY-MM-DD
        
        title Timeline-Capstone-Part-B 
        
        section Time-Allocated
        Holiday                     :done, weekNull, 2018-07-02, 7d
        Week 00                     :done, week0, 2018-07-09, 7d
        Week 01                     :done, week1, 2018-07-16, 7d
        Week 02                     :done, week2, 2018-07-23, 7d
        Week 03                     :done, week3, 2018-07-30, 7d
        Week 04                     :active, week4, 2018-08-06, 7d
        Week 05                     :active, week5, 2018-08-13, 7d
        Week 06                     :active, week6, 2018-08-20, 7d
        Break Week                  :active, weekBreak, 2018-08-27, 7d
        Week 07                     :active, week8, 2018-09-03, 7d
        Week 08                     :active, week9, 2018-09-10, 7d
        Week 09                     :active, week10, 2018-09-17, 7d
        Week 10                     :active, week11, 2018-09-24, 7d
        Week 11                     :active, week12, 2018-10-01, 7d
        Week 12                     :active, week13, 2018-10-08, 7d
        Week 13                     :active, week14, 2018-10-15, 7d
    
        section Assesment-Tasks
        Completion Plan         :crit, after week3, 7d 
        Proffesional Practice & Contribution :crit, after week12, 4d
        Final Report :crit, after week11, 7d
        Presentation :crit, after week13, 3d

        section Software-Android
        Joining Protocol Re-Oriented :done, after weekNull, 3d
        Discovery Protocol Prototype :done, 7d
        Testing Joining Interaction :done , 7d
        Testing Discovery Interaction :active, 7d
        Software design on the fetching the metric :active, 7d
        Verification on Joining & Discovery Interaction :active, 12d
        Documentation :active, 3d
        Realtime Graph Adapter: active, 7d
        Data Fetch from the API inside from the MCU :active, 7d

        section Software-ESP8266
        Re-Oriented Joining Protocol :done, after weekNull, 3d
        Discovery Protocol Integration :done, 7d
        Integrating Joining and Discovery :done, 7d
        Design on a bounce diagram on metric :active, 7d
        Documentation :active, 3d
        Software to send out metrics every 1 second :active, 7d
        Buffer Implementation to Record Humid and Temp Every Hour In The MCU :active, 7d
        Buffer Implementation to Record Humid and Temp Wihtin the last two hours with resolution of 1 minutes :active , 7d

        section Hardware-PCB
        Testing Relay :done, after weekNull, 3d
        Reoriented PCB Position :done, 3d
        Consulted PCB Position :done, 3d
        Finalizing PCB :done, PCBFinalized, 2018-07-20,4d
        Deploy PCB to production :active, FinalizingPCB, 2018-07-24, 20d
        MidPoint PCB Deployment Days :active , MidPoint, 1d
        Assembly :active, 7d
        Testing PCB :active, 10d
        Validation :active , 10d

        section Ordering-Hardware
        Order and buy waterproof temperature sensor :active, after MidPoint, 14d
        Order and buy enclosure for wireless sensor :active, after MidPoint, 7d
        Order and buy the input terminals :active, after MidPoint, 7d


```