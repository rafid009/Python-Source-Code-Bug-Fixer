import numpy as np 

def function(x):

	p0 = x
	v7 = 6
	paths = []
	try:
		if x > 6:
			v7 = 3+v7
			paths.append(1)
		else:
			p0 = 2+x
			v7 = 2-v7
			paths.append(2)
		if v7 <= 9:
			x = x/v7
			v7 = 8/v7
			paths.append(3)
		else:
			v7 = 4*x
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))