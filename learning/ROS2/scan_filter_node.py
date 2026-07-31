import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanFilterNode(Node):
    def __init__(self):
        super().__init__('scan_filter_node')
        self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

    def scan_callback(self, msg):
        ranges = msg.ranges
        closest = float('inf')
        for item in ranges:
            if item > msg.range_min and item < msg.range_max:
                if item < closest:
                    closest = item
        self.get_logger().info(f"Closest: {closest}")

def main():
    rclpy.init()
    node = ScanFilterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
