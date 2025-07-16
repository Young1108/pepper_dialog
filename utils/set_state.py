import qi
import sys
from connection import PepperConnection

class State:
    def __init__(self, session):
        self.session = session
        self.motion_service = self.session.service("ALMotion")
        self.autonomous_life_service = self.session.service("ALAutonomousLife")


    def set_state(self, state):
        """
        设置 Pepper 的状态。

        参数:
        - state: 期望设置的状态，可以是 'wake', 'rest', 'solitary', 'interactive', 'safe', 'disabled'。
        """
        if state == "safe": self.autonomous_life_service.setState("safeguard")
        # match state:
        #     case 'wake':
        #         self.motion_service.wakeUp()
        #     case 'rest':
        #         self.motion_service.rest()
        #     case 'solitary':
        #         self.autonomous_life_service.setState("solitary")
        #     case 'interactive':
        #         self.autonomous_life_service.setState("interactive")
        #     case 'safe':
        #         self.autonomous_life_service.setState("safeguard")
        #     case 'disabled':
        #         self.autonomous_life_service.setState("disabled")
        #     case _:
        #         print(f"State '{state}' not recognized.")
        print(f"Pepper's now state: {state}.")

if __name__ == "__main__":
    ip_address = "192.168.192.106"
    pepper_connection = PepperConnection()

    session = pepper_connection.connect_to_robot_ip(ip_address)

    state_manager = State(session)

    desired_state = "safe"

    state_manager.set_state(desired_state)


'''
当Pepper处于'rest'状态时，机器人会停止所有运动并关闭电机，进入一种节能模式。
在这种状态下，Pepper的关节不会保持任何特定姿势，机器人的电机不会维持力量输出。

'disabled'状态,停用自主生活特性，这意味着Pepper将不会自主地进行交互、探索环境或响应外部刺激。
这并不意味着机器人进入了休眠或节能模式，而是简单地停用了某些自主行为。
当被唤醒时，保持站立姿势
'''