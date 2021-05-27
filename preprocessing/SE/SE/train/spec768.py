import numpy as np 

def function(x):

	p2 = 0
	o6 = 6
	paths = []
	try:
		if o6 >= 5:
			x = x*5
			paths.append(1)
		else:
			o6 = 2*o6
			paths.append(2)
		if o6 > 3:
			o6 = p2-o6
			paths.append(3)
		else:
			o6 = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))