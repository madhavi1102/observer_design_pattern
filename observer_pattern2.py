"""
Different Group of subscribers register to a publisher
the publisher invokes different subscriber object and it's respective method
"""
class SubscriberGrpOne:

    def __init__(self, name):
        self.name = name

    #action
    def update(self, message):
        print(f"{self.name} got the message {message}")

class SubscriberGrpTwo:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f"{self.name} receive message {message}")


class Publisher:

    def __init__(self):
        self.subscribers = dict()
    def register(self, subscriber, callback=None):
        if callback is None:
            callback = getattr(subscriber, 'update')   # works only for object of SubscriberGrpOne
        self.subscribers[subscriber] = callback

    def unregister(self, subscriber):
        del self.subscribers[subscriber]

    def publish(self, message):
        for sub, callback in self.subscribers.items():
            callback(message)



pub = Publisher()

alice = SubscriberGrpOne("Alice")
bob = SubscriberGrpTwo("Bob")
john = SubscriberGrpOne("John")

pub.register(alice, alice.update)
pub.register(bob, bob.receive)
pub.register(john)

pub.publish("Welcome! greeting ")
pub.unregister(bob)

pub.publish("Modified the subscribers ")






