"""
This is the simplest approach of implementing Observer Design pattern
Object maintains a list of dependent objects, called subscriber.
 The object notifies other objects to do action in response, by directly calling the subscriber method only.

 What this program is doing:
 1. one publisher object sends a common notification to all it's subscribers
 like a newsletter notification. all the subscribers get the same notification message from the  publisher.
"""

class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"{self.name} got message {message}")

class Publisher:

    def __init__(self):
        self.subscribers = set()

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish(self, message):
        for sub in self.subscribers:
            sub.update(message)


pub = Publisher()

alice = Subscriber("Alice")
bob  = Subscriber("Bob")
cat = Subscriber("Cat")

pub.register(alice)
pub.register(bob)
pub.register(cat)

pub.publish("Welcome, happy day!")

pub.unregister(alice)
pub.publish("Event occurred!")