import numpy as np 

def function(x):

	k2 = 9
	p9 = 6
	x = x
	paths = []
	try:
		if k2 >= 2:
			p9 = 7+p9
			paths.append(1)
		else:
			k2 = k2/k2
			paths.append(2)
		if x > 9:
			x = x-7
			x = x*6
			paths.append(3)
		else:
			p9 = p9/7
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