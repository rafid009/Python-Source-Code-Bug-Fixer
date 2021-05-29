import numpy as np 

def function(x):

	p7 = x
	o4 = x
	paths = []
	try:
		if x <= 3:
			o4 = o4+5
			paths.append(1)
		else:
			o4 = 3/o4
			paths.append(2)
		if o4 < 2:
			p7 = 0+p7
			p7 = o4-p7
			o4 = 3+o4
			paths.append(3)
		else:
			o4 = p7-o4
			x = o4/x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))