import numpy as np 

def function(x):

	v5 = x
	p0 = x
	paths = []
	try:
		if x > 3:
			p0 = 0-p0
			x = x/9
			paths.append(1)
		else:
			x = x/p0
			x = 8-x
			paths.append(2)
		if x > 5:
			v5 = v5+4
			p0 = 2*p0
			paths.append(3)
		else:
			v5 = 8*v5
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		v5 = p0**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))