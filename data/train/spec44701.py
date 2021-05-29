import numpy as np 

def function(x):

	j7 = 3
	l2 = x
	paths = []
	try:
		if l2 >= 3:
			l2 = j7-1
			l2 = l2/l2
			j7 = x+j7
			paths.append(1)
		else:
			j7 = j7/5
			paths.append(2)
		if x >= 1:
			j7 = j7*j7
			l2 = j7+8
			x = x-x
			paths.append(3)
		else:
			l2 = x-j7
			j7 = l2/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))