import numpy as np 

def function(x):

	p0 = x
	v6 = x
	paths = []
	try:
		if x >= 9:
			p0 = p0/5
			paths.append(1)
		else:
			p0 = p0-9
			paths.append(2)
		if p0 >= 3:
			x = 6/6
			x = x+v6
			paths.append(3)
		else:
			p0 = p0*6
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		x = v6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))