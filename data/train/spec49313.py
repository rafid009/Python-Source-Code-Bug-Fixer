import numpy as np 

def function(x):

	o7 = 6
	p3 = 0
	paths = []
	try:
		if p3 > 0:
			o7 = o7+p3
			x = x+o7
			paths.append(1)
		else:
			x = x+o7
			o7 = o7-2
			paths.append(2)
		if o7 <= 5:
			p3 = o7*5
			p3 = 2-2
			paths.append(3)
		else:
			x = 5-x
			o7 = o7-o7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))