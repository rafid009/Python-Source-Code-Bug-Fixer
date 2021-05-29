import numpy as np 

def function(x):

	v9 = x
	l2 = 2
	x = 0
	paths = []
	try:
		if l2 >= 5:
			v9 = 7-v9
			v9 = v9+0
			paths.append(1)
		else:
			l2 = l2-v9
			l2 = x+3
			paths.append(2)
		if l2 >= 0:
			x = x-2
			paths.append(3)
		else:
			l2 = 9-6
			v9 = v9*l2
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))