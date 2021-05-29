import numpy as np 

def function(x):

	p6 = 8
	a5 = 1
	paths = []
	try:
		if p6 <= 9:
			x = 7-x
			p6 = 0-a5
			paths.append(1)
		else:
			a5 = x/1
			p6 = p6/5
			paths.append(2)
		if x < 7:
			a5 = a5*8
			a5 = 2*3
			p6 = p6-9
			paths.append(3)
		else:
			a5 = a5/x
			a5 = a5*9
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