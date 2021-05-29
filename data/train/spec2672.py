import numpy as np 

def function(x):

	a8 = x
	l3 = x
	x = x
	paths = []
	try:
		if a8 >= 4:
			x = l3-2
			paths.append(1)
		else:
			l3 = l3*l3
			x = 6/x
			x = x/4
			paths.append(2)
		if a8 < 5:
			x = l3-x
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))