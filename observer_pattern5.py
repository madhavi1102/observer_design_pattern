""""

1. Different subscriber groups
2. multiple events of a publisher
3. subscriber also knows about the event
4. To avoid sending event name in the message

"""


class SubscriberGP1:

    def __init__(self, name: str):
        self.name = name

    def update(self, message: str, event: str) -> None:
        print(f"{self.name} got message for event {event} => {message}")


class SubscriberGP2:

    def __init__(self, name):
        self.name = name

    def receive(self, message: str, event: str):
        print(f"{self.name} got message from event {event} => {message}")


class Publisher:

    def __init__(self, events: list[str]):
        self.events = events
        self._subscribers = {event: dict() for event in events}


    def get_subscribers(self):
        return self._subscribers

    def register(self, event, subscriber, callback=None):
        if event not in self.events:
            return f"Event {event} does not exist!"
        if callback is None:
            callback = getattr(subscriber, 'update')
        self._subscribers[event][subscriber] = callback

    def unregister(self, event, subscriber):
        if event not in self.events:
            return f"Event {event} does not exist!"
        del self._subscribers[event][subscriber]

    def publish(self, event, message):
        for sub, callback in self._subscribers[event].items():
            callback(message, event)


p = Publisher(["Food", "Trip", "Exhibition"])

a = SubscriberGP2("A")
b = SubscriberGP1("B")
c = SubscriberGP2("C")
d = SubscriberGP1("D")
e = SubscriberGP1("E")


p.register("Food", a, a.receive)
p.register("Trip", b, b.update)
p.register("Trip", c, c.receive)
p.register("Exhibition", d, d.update)
p.register("Exhibition", e)

p.publish("Food", "Food Event at 10 Am")
p.publish("Trip", "Trip started tomorrow")
p.publish("Exhibition", "Images Exhibition in Pune")