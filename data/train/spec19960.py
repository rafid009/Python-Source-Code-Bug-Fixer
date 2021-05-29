import numpy as np 

def function(x):

	o6 = x
	q6 = 2
	paths = []
	try:
		if x <= 4:
			q6 = x-1
			x = x/4
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x >= 5:
			q6 = q6-2
			q6 = 4-q6
			x = x+o6
			paths.append(3)
		else:
			x = x/x
			q6 = q6+7
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))