import numpy as np 

def function(x):

	a2 = 3
	p9 = 3
	paths = []
	try:
		if a2 >= 9:
			x = p9-4
			paths.append(1)
		else:
			p9 = 8+p9
			paths.append(2)
		if a2 <= 1:
			p9 = p9-a2
			x = x*a2
			paths.append(3)
		else:
			x = 4/x
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