from robot import APOSRobot


robot3 = APOSRobot("APOS-001")
robot2 = APOSRobot("APOS-002")
robot8 = APOSRobot("APOS-008")

print(robot3.name)
print(robot2.name)
print(robot8.name)
robot8.experience("success")
robot8.experience("failed")
robot3.experience("success")
robot2.experience("failed")
robot3.experience("praised")


print(robot3.traits)
print(robot3.memory.memories)
print(robot2.traits)
print(robot2.memory.memories)
print(robot8.traits)
print(robot8.memory.memories)