import numpy as np 

def function(x):

	j7 = 0
	l7 = 2
	paths = []
	try:
		if l7 > 5:
			j7 = j7+7
			paths.append(1)
		else:
			j7 = 9/6
			x = 0-x
			x = x-7
			paths.append(2)
		if x <= 4:
			x = 6/x
			j7 = j7-8
			paths.append(3)
		else:
			j7 = 0*j7
			j7 = 4+j7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))