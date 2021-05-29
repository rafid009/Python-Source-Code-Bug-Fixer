import numpy as np 

def function(x):

	p4 = x
	o5 = 2
	paths = []
	try:
		if x <= 2:
			o5 = 8/7
			o5 = o5*o5
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if p4 > 3:
			o5 = 5+o5
			paths.append(3)
		else:
			x = 0-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))