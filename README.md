APOS-V.0001

APOS-V.0001 is an early Python prototype for an Artificial Personality Operating System. It models robots whose personality traits change after experiences and whose recognized experiences are stored in memory.

PROJECT FILES

robot.py defines the APOSRobot class. Each robot has a name, its own Memory object, personality traits, cognitive traits, and event-driven trait changes. Its methods can display traits, adjust trust, process experiences, keep changed traits between 0 and 100, and save recognized events.

memory.py defines the Memory class. It stores event names in a list called memories through the add_memory(event) method.

main.py is the demonstration program. It creates three robots, gives them different experiences, and prints their resulting traits and memories. This shows that each robot develops independently.

HOW TO RUN THE DEMO

APOS-V.0001 requires Python 3 and does not use external packages.

1. Clone the repository:
   git clone https://github.com/slimreaperwoj/APOS-V.0001.git

2. Open the project folder:
   cd APOS-V.0001

3. Run the demo:
   python main.py

CURRENT STATUS

The current robot.py file has missing commas around the praised and insulted event definitions. Python will raise a syntax error before the demo starts. Those dictionary entries must be corrected before main.py can run.

TRAITS

All traits begin at 50. Personality traits changed by experiences are kept within the range of 0 to 100.

Curiosity: Willingness to explore, investigate, and learn.

Patience: Ability to tolerate delays, difficulty, or repeated attempts.

Trust: Willingness to rely on people or information.

Confidence: Belief in the robot's ability to act successfully.

Sociability: Tendency to interact and connect with others.

Persistence: Willingness to continue after difficulty or failure.

Caution: Tendency to consider risk before acting.

Intelligence: General reasoning and problem-solving ability.

Creativity: Ability to produce original ideas or approaches.

Knowledge: Amount of learned information available to the robot.

Intelligence, creativity, and knowledge are stored separately as cognitive traits. Events do not change them in this version.

EVENTS

success
Changes: curiosity +2, confidence +3, persistence +2.
Meaning: A successful outcome encourages exploration, self-belief, and continued effort.

failed
Changes: patience -2, confidence -3, persistence +1.
Meaning: Failure causes frustration and reduced confidence but slightly strengthens determination.

praised
Changes: sociability +1, confidence +2, trust +1.
Meaning: Positive feedback makes the robot more social, confident, and trusting.

insulted
Changes: trust -5, curiosity -2.
Meaning: Negative treatment makes the robot less trusting and less willing to engage or explore.

Only recognized events change traits and enter memory. An unknown event name prints a warning and makes no changes.

EXAMPLE

from robot import APOSRobot

robot = APOSRobot("APOS-001")
robot.experience("success")

print(robot.traits)
print(robot.memory.memories)

After the success event, the robot's curiosity is 52, confidence is 53, persistence is 52, and its memory contains "success".
