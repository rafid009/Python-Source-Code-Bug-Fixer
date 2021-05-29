import numpy as np 

def function(x):

	o7 = 6
	p1 = x
	paths = []
	try:
		if x > 9:
			x = 2/x
			paths.append(1)
		else:
			o7 = 1-o7
			x = x+1
			paths.append(2)
		if x < 1:
			x = x/o7
			paths.append(3)
		else:
			x = 7+1
			o7 = p1*p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))