# 🛠️ ros_basics

A ROS 2 package showcasing the **core building blocks** of ROS 2 using `rclpy` (Python).  
Ideal for learners, interview prep, and quick prototyping.

---

## 📚 Features

This package demonstrates the following ROS 2 concepts:

| Component           | Description                                                        |
|---------------------|--------------------------------------------------------------------|
| ✅ Publisher         | Publishes a `String` or `Twist` message at a regular interval      |
| ✅ Subscriber        | Listens to a topic and logs received messages                      |
| ✅ Service (Server)  | Implements a service (e.g. add two ints, echo string)              |
| ✅ Service (Client)  | Calls the service and prints the response                          |
| ✅ Action (Server)   | Executes a long-running goal like countdown or Fibonacci           |
| ✅ Action (Client)   | Sends goal requests to the action server                           |
| ✅ Parameters        | Reads and sets node parameters dynamically                         |
| ✅ Custom Interface  | Uses `.msg`, `.srv`, or `.action` files to define custom types     |

---


## 🧱 Package Structure

```
    ros_basics/
    ├── package.xml
    ├── setup.py
    ├── resource/
    ├── ros_basics/
    │   ├── __init__.py
    │   ├── publisher_node.py
    │   ├── subscriber_node.py
    │   ├── service_server.py
    │   ├── service_client.py
    │   ├── action_server.py
    │   ├── action_client.py
    │   ├── parameter_node.py
    ├── msg/
    │   └── CustomMessage.msg
    ├── srv/
    │   └── AddTwoInts.srv
    ├── action/
    │   └── Countdown.action
```

## Run Examples

Publisher:
``` ros2 run ros_basics talker ```

Subscriber:
``` ros2 run ros_basics listener ```





