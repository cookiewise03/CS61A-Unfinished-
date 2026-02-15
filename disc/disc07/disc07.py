#1.2

class MinList:
    """一个仅能弹出最小元素的列表"""
    def __init__(self):
        self.items = []
        self.size = 0

    def append(self, item):
        """向Minlist中添加一个元素
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items += item
        self.size += 1

    def pop(self):
        """移除并返回Minlist中的最小元素
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        for index in range(self.size):
            if self.items[index] == min(self.items):
                self.size -= 1
                return self.items.pop(index)

#1.3

class Email:
    """每个邮件对象都有三个实例属性：
    邮件内容、发件人姓名、收件人姓名。
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """每个服务器对象都有一个实例属性clients，
    该属性是一个字典，将客户端姓名映射到对应的客户端对象。
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """接收一封邮件，并将其放入收件客户端的收件箱中。
        """
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """接收一个客户端对象和对应的客户端姓名，
        将其添加到clients实例属性中。
        """
        self.clients[client_name] = client

class Client:
    """每个客户端对象都有以下实例属性：
    name（用于指定邮件的收件客户端）、
    server（用于向其他客户端发送邮件）、
    inbox（存储客户端收到的所有邮件的列表）。
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name

    def compose(self, msg, recipient_name):
        """发送一封邮件，邮件内容为指定的msg，
        收件人为指定的客户端。
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """接收一封邮件，并将其添加到该客户端的收件箱中。
        """
        self.inbox.append(email)

#2.1

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True  # 它是活的！
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(name, owner)
        self.lives = lives

    def talk(self):
        """ 打印猫的问候语
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')

    def lose_life(self):
        """将猫的生命值减1。
        当生命值变为0时，将is_alive属性设为False。
        若生命值已为0时调用该方法，打印提示信息表示猫已无生命值可扣。
        """
        if self.lives > 0:
            self.lives -= 1
        else:
            print('This cat has no more lives to lose.')

#2.2

class NoisyCat(Cat):  # 补全此处！
    """一只会重复说两遍话的猫"""
    def __init__(self, name, owner, lives=9):
        # 这个方法是必要的吗？为什么？
        Cat.__init__(name, owner, lives)

    def talk(self):
        """叫声是普通猫的两倍
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        Cat.talk(self)
        Cat.talk(self)

    def __repr__(self):
        """吵闹的猫的解释器可读表示形式
        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')
        """
        return "NoisyCat('{}', '{}')".format(self.name, self.owner)