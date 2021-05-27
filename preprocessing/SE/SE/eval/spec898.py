import numpy as np 

def function(x):

	h9 = x
	j3 = x
	paths = []
	try:
		if x > 3:
			j3 = j3/7
			paths.append(1)
		else:
			j3 = 0-j3
			paths.append(2)
		if x < 4:
			h9 = h9-7
			h9 = 5+7
			paths.append(3)
		else:
			h9 = h9*7
			x = 4/9
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))