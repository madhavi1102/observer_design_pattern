### Behavioral Design Patttern -> Observer Pattern

Observer Pattern is a behavioral design pattern in which an object notifes to all the other objects as its dependent with any change of state. 
This repo contains illustration of event-driven programming in simple python scripts using observer pattern.

The Event driven applications we see in most of the real world applications. Event simply refers to any change in state.      For example 
- Many users when subscribed to a newsletter, get a notification over mail or any other service whenever the author of the blog updates a post or adds a new post. 
- A user when completes a payment. The bill is received to its message or mail account.

By Definition in Wikipedia:
The Observer Design pattern is a software design pattern in which an object, called the subject, maintains a list o f its dependents , called observers, and notifies them automatically of any state change, by calling one of their methods.

The benefits of the event-driver programming are
- Loose coupling of various modules or application or services
- Modular design and easy handling and debugging 

Python provides an easy and efficient way to implement observer design pattern because of its special features as:
- Dynamic typing
- Functions as first class objects
- object variables are reference to the heap stored objects
- class also has a reference


 Different possible scenarios to observer design pattern are covered here.
1. A publisher sends out notification to all its subscribed members.
2. Different groups are subscribed to a publisher, and the publisher accordingly notifies to subscriber with different messages.
3. A publisher manages multiple events and different subscribers are registered to different events. For an event, publisher sends out notification to only event registered subscribers.
4. Subscribers are not necessary to know about the publisher, however, publisher can send information about itself and event to subscriber.


Future Improvement:

This approach holds strong reference of subscriber objects to the subject which can cause memory leak and is not suitable for large scale web applications. Observers and  subjects should be decoupled, means totally unaware of each other. This can be acheived though Message Queue or Message topic broker which acts as middle layer between  publishers and subscribers. Whenever a message is pushed to topic, immediately all the associated subscribers are notified.


