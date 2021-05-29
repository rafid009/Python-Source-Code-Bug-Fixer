import numpy as np 

def function(x):

	p0 = 0
	u4 = x
	paths = []
	try:
		if u4 >= 8:
			p0 = 7/9
			u4 = 4+u4
			p0 = 8+p0
			paths.append(1)
		else:
			x = x*8
			x = p0-6
			u4 = x-3
			paths.append(2)
		if p0 < 3:
			x = p0*u4
			u4 = u4-x
			paths.append(3)
		else:
			x = u4*x
			p0 = p0-5
			p0 = p0-1
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))