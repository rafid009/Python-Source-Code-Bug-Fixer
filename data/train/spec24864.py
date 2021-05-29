import numpy as np 

def function(x):

	j5 = x
	q7 = 1
	paths = []
	try:
		if q7 >= 5:
			x = 3/7
			q7 = 1/q7
			paths.append(1)
		else:
			j5 = j5/6
			j5 = j5+8
			paths.append(2)
		if x <= 9:
			x = x+2
			paths.append(3)
		else:
			q7 = 7/q7
			q7 = x/q7
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))