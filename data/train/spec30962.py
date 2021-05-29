import numpy as np 

def function(x):

	p9 = x
	a3 = 9
	paths = []
	try:
		if a3 < 6:
			x = 1/x
			x = x-4
			a3 = p9/1
			paths.append(1)
		else:
			a3 = a3/p9
			paths.append(2)
		if p9 < 2:
			p9 = p9*p9
			paths.append(3)
		else:
			p9 = x+p9
			p9 = 0*p9
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))