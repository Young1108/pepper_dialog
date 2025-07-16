'''
interface:
    1. 创建APP和Session，建立与Pepper的连接
    2. 返回Pepper的会话对象Session

'''

import qi
import sys

class PepperConnection:
    def __init__(self):
        self.robot_ip = None
        self.robot_port = 9559  # defualt port, don't change
        self.app = None
        self.session = None

    def connect_to_robot_ip(self, robot_ip):
        """连接到Pepper机器人"""
        self.robot_ip = robot_ip
        try:
            self.app = qi.Application(["RobotApp2", "--qi-url=tcp://" + self.robot_ip + ":" + str(self.robot_port)])
            self.app.start()
            self.session = self.app.session
            print("Session created.")
            print(f"成功连接到 Pepper @{self.robot_ip}:{self.robot_port}")
            
            return self.session
        
        except Exception as e:
            print(f"连接Pepper时发生错误: {e}")
            sys.exit(1)


# test
if __name__ == "__main__":
    ip_address = "10.108.11.12"
    pepper_connection = PepperConnection()
    pepper_connection.connect_to_robot_ip(ip_address)
    session = pepper_connection.get_session()