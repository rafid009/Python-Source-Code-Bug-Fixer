import numpy as np 

def function(x):

	l5 = 8
	v7 = 0
	paths = []
	try:
		if x < 6:
			l5 = x+l5
			v7 = x-v7
			l5 = l5-0
			paths.append(1)
		else:
			x = x+6
			v7 = v7/l5
			paths.append(2)
		if x >= 7:
			x = 2/x
			paths.append(3)
		else:
			v7 = 7+l5
			l5 = l5+x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))