import numpy as np 

def function(x):

	p0 = x
	x7 = 5
	paths = []
	try:
		if x7 > 2:
			x7 = x7*6
			x = x*4
			paths.append(1)
		else:
			p0 = p0*x7
			p0 = 0+p0
			p0 = 3+9
			paths.append(2)
		if x7 <= 4:
			x = 0-x
			x = x/x
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x7 = p0**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))