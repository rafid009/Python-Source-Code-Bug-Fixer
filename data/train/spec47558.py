import numpy as np 

def function(x):

	q1 = 2
	j7 = x
	paths = []
	try:
		if x >= 9:
			j7 = j7*x
			paths.append(1)
		else:
			x = 4+3
			paths.append(2)
		if j7 < 5:
			x = x-4
			x = 7*x
			paths.append(3)
		else:
			x = q1-0
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))