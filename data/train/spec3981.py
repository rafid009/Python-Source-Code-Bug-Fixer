import numpy as np 

def function(x):

	y5 = x
	l4 = 1
	x = 5
	paths = []
	try:
		if y5 < 5:
			y5 = y5+4
			paths.append(1)
		else:
			l4 = l4*0
			paths.append(2)
		if x < 4:
			y5 = x-6
			paths.append(3)
		else:
			x = 8-3
			x = x-x
			x = y5*x
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		l4 = y5**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))