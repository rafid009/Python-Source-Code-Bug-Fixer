import numpy as np 

def function(x):

	a2 = 2
	g9 = x
	paths = []
	try:
		if g9 >= 8:
			x = a2-2
			x = 6-x
			paths.append(1)
		else:
			a2 = x*a2
			paths.append(2)
		if g9 > 3:
			x = x+a2
			x = x/3
			x = x*6
			paths.append(3)
		else:
			a2 = 2*a2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))