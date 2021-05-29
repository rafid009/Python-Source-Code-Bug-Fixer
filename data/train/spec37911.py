import numpy as np 

def function(x):

	n4 = 4
	l5 = 4
	paths = []
	try:
		if l5 > 4:
			n4 = n4*5
			n4 = 5+8
			x = x+4
			paths.append(1)
		else:
			n4 = n4*3
			x = x-0
			paths.append(2)
		if l5 >= 1:
			n4 = n4-9
			n4 = n4-2
			n4 = n4+n4
			paths.append(3)
		else:
			x = x-2
			l5 = 7*l5
			l5 = x*l5
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