import numpy as np 

def function(x):

	p3 = 2
	a3 = x
	x = x
	paths = []
	try:
		if x >= 6:
			x = x+7
			paths.append(1)
		else:
			p3 = 8/x
			paths.append(2)
		if a3 <= 0:
			a3 = a3-0
			paths.append(3)
		else:
			p3 = 3*9
			a3 = a3/x
			x = 6-p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		a3 = p3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))