class Publisher:

    def __init__(self, event: str):
        self.event = event
        self.subscribers = set()

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message, self)



class Subscriber:

    def __init__(self, name: str):
        self.name = name
    def update(self, message, subject: Publisher):
        print(f"{self.name} receives notification from {subject.event}:::::=>  {message}")



p = Publisher("food")

mary = Subscriber("Mary")
kivy = Subscriber("Kivy")

p.register(mary)
p.register(kivy)

p.publish("Great time at Work!")

p.unregister(kivy)

p.publish("Break time! See ya")


