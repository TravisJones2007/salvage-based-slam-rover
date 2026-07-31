Notes
-self is a placeholder variable that can become whatever object the method is called upon
self.get_logger-> go into self(whatever that may be at the time) and access get_logger
class=defines what the node is and what it can do, main() is a seperate function outside of the class that actually creates and runs the node

Node is ROS2's imported blueprint with all of the built components, MyFirstNode is my own blueprint that builds upon Node and adds my specific behaviours

investigated Laserscan data types and structure, ranges = list of distances, range_min and range_max -> discard readings outside of these, angle_min/angle_increment -> tells you where each reading points too.
