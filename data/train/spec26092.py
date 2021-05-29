import numpy as np 

def function(x):

	o3 = x
	p0 = x
	paths = []
	try:
		if x >= 5:
			o3 = 0+p0
			p0 = 8/7
			x = o3/x
			paths.append(1)
		else:
			o3 = o3+o3
			p0 = p0+x
			paths.append(2)
		if p0 > 2:
			x = 6*x
			p0 = 3-5
			o3 = 0-o3
			paths.append(3)
		else:
			x = x+p0
			p0 = p0*p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))