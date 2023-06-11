"""
Publisher has multiple events.
Each event has dictionary of subscribers and it's method attribute callable.
So when a publisher publishes on an event, only it's subscribed members get the notification
"""


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} got the message {message}")


class Publisher:
    def __init__(self, events: list[str]):
        self.events = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, subscriber, callback):
        if event not in self.events:
            return
        if callback is None:
            callback = getattr(subscriber, 'update')
        self.events[event][subscriber] = callback

    def unregister(self, event, subscriber):
        del self.events[event][subscriber]

    def publish(self, event, message):
        for sub, callback in self.get_subscribers(event).items():
            callback(message)




p = Publisher(["food","games"])

madhv = Subscriber("Madhv")
krishna = Subscriber("Krishna")
john = Subscriber("John")

p.register("food", madhv, madhv.update)
p.register("games", krishna, krishna.update)
p.register("food", john, john.update)

p.publish("food", "Food Event Notification")
p.publish("games", "Game Event Notification")

p.unregister("food", madhv)

p.publish("food","Event Food changed!")
