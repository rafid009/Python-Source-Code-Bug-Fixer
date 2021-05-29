import numpy as np 

def function(x):

	p9 = 4
	a7 = 9
	paths = []
	try:
		if x <= 5:
			p9 = x*p9
			paths.append(1)
		else:
			x = x/3
			x = 9*1
			x = x-4
			paths.append(2)
		if x <= 3:
			a7 = a7-6
			x = 3-9
			paths.append(3)
		else:
			a7 = a7/5
			a7 = a7-7
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