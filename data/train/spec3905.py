import numpy as np 

def function(x):

	b8 = 5
	j7 = x
	paths = []
	try:
		if x >= 6:
			b8 = 4*b8
			j7 = 5-j7
			paths.append(1)
		else:
			j7 = x/j7
			b8 = b8-x
			x = x+0
			paths.append(2)
		if j7 > 2:
			x = 0/x
			paths.append(3)
		else:
			j7 = j7+2
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