import numpy as np 

def function(x):

	l4 = 3
	n2 = x
	paths = []
	try:
		if l4 < 5:
			l4 = 5/6
			l4 = 1-l4
			paths.append(1)
		else:
			l4 = 1*l4
			x = x/3
			l4 = l4/1
			paths.append(2)
		if x < 4:
			x = x/8
			x = x*8
			paths.append(3)
		else:
			n2 = 0*n2
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