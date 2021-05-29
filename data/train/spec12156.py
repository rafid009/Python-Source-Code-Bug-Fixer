import numpy as np 

def function(x):

	p6 = 5
	a7 = x
	paths = []
	try:
		if x <= 3:
			p6 = 3-p6
			paths.append(1)
		else:
			a7 = 9+a7
			a7 = a7-a7
			x = x/x
			paths.append(2)
		if a7 >= 3:
			a7 = a7/5
			x = 1-p6
			p6 = p6*4
			paths.append(3)
		else:
			x = x/p6
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		p6 = a7**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))