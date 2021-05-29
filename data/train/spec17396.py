import numpy as np 

def function(x):

	a0 = x
	l3 = 3
	paths = []
	try:
		if l3 <= 2:
			l3 = l3/x
			x = x/a0
			paths.append(1)
		else:
			l3 = l3*5
			x = 9+x
			x = 3-x
			paths.append(2)
		if a0 >= 2:
			x = x*6
			l3 = x*l3
			paths.append(3)
		else:
			x = x+6
			x = x-l3
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))