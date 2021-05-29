import numpy as np 

def function(x):

	l3 = x
	b8 = x
	paths = []
	try:
		if l3 < 3:
			b8 = b8*7
			paths.append(1)
		else:
			x = x*l3
			l3 = 9*6
			paths.append(2)
		if l3 < 9:
			l3 = 2*6
			paths.append(3)
		else:
			l3 = 1*x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))