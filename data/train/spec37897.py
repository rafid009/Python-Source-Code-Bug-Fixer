import numpy as np 

def function(x):

	v6 = x
	p0 = 9
	paths = []
	try:
		if p0 > 0:
			x = p0-0
			x = 3/v6
			paths.append(1)
		else:
			p0 = 8*p0
			p0 = 3-p0
			paths.append(2)
		if x < 4:
			p0 = p0+4
			paths.append(3)
		else:
			v6 = 5/x
			p0 = p0-x
			v6 = v6-4
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