import numpy as np 

def function(x):

	q5 = 0
	e9 = 6
	paths = []
	try:
		if x >= 3:
			e9 = e9*9
			paths.append(1)
		else:
			e9 = e9*e9
			paths.append(2)
		if x >= 4:
			q5 = 7+q5
			paths.append(3)
		else:
			q5 = q5+x
			e9 = 7-2
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		e9 = q5**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))