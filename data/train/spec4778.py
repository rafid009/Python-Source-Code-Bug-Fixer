import numpy as np 

def function(x):

	p0 = 0
	v2 = x
	paths = []
	try:
		if p0 > 7:
			p0 = p0+4
			v2 = 9+0
			paths.append(1)
		else:
			p0 = p0/2
			x = 8/x
			paths.append(2)
		if x >= 0:
			v2 = v2*v2
			p0 = p0+p0
			paths.append(3)
		else:
			v2 = v2*1
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))