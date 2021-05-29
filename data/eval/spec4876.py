import numpy as np 

def function(x):

	u6 = 8
	j7 = x
	paths = []
	try:
		if x < 1:
			u6 = 9-4
			u6 = u6+4
			paths.append(1)
		else:
			j7 = x-8
			x = x+j7
			paths.append(2)
		if u6 <= 3:
			j7 = 9*j7
			paths.append(3)
		else:
			j7 = 1/j7
			u6 = u6/5
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