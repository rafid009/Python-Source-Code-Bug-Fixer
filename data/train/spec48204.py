import numpy as np 

def function(x):

	p3 = 9
	o6 = 1
	paths = []
	try:
		if x > 5:
			x = 1/o6
			paths.append(1)
		else:
			o6 = x+o6
			o6 = o6+o6
			p3 = 6-p3
			paths.append(2)
		if x >= 8:
			p3 = p3/7
			x = x*x
			o6 = p3+o6
			paths.append(3)
		else:
			p3 = p3-x
			p3 = p3/o6
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