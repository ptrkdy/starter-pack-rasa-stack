# this is a module for layered conversations

# it must support conversations with different stages
# it must support the ability to change between stages

# it could support changing the weights of various actions when at particular stages
# e.g. classification (gathering information)
# e.g. providing information
# e.g. stored background state (for example, name, address etc)

# it should support pipelines, which should be a collection of question queues or magazines

# it should support a mechanism to jump around between the magazines

# there should probably be a sort of "attention span" metric that the bot has, and if it becomes "confused" it should reset stage

# perhaps this can be combined into a set of priority queues

# a multilevel stage is a set of relationships between questions in the pipeline, could be natural transition points

class MultiLevelStage():
	def __init__(self):
		self.levels = [1, 2, 3]
		self.current_level = self.levels[0]
		self.backaction = "someAction"

	def change_level(arg1):
		self.current_level = self.level[arg1]
		print("Change levels {}", arg1)


# a pipeline is a collection of magazines

class Pipeline():
	def __init__(self):
		self.magazines = []
		self.start = "test"
		self.middle = "test"
		self.end = "test"

	def change_pipeline():
		print("update pipeline")


# a magazine should be a stack of key value entities, the keys being the previous question?

class Magazine():
	def __init__(self):
		self.questions = {"question1": "first question", "question2": "second question"}

