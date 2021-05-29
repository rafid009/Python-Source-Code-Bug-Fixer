import numpy as np 

def function(x):

	p9 = 0
	a3 = 0
	paths = []
	try:
		if a3 <= 4:
			a3 = a3*7
			a3 = a3+3
			x = 7-x
			paths.append(1)
		else:
			a3 = a3-7
			x = x-a3
			x = x/x
			paths.append(2)
		if a3 <= 0:
			p9 = 4-p9
			p9 = 2+p9
			p9 = 5+p9
			paths.append(3)
		else:
			a3 = 7-4
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