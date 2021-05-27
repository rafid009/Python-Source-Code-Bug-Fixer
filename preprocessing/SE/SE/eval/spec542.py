import numpy as np 

def function(x):

	p0 = x
	r8 = x
	paths = []
	try:
		if x >= 0:
			p0 = p0+8
			x = x*3
			x = x*0
			paths.append(1)
		else:
			r8 = 5/p0
			r8 = r8+6
			paths.append(2)
		if x < 7:
			p0 = p0*5
			x = x-x
			paths.append(3)
		else:
			p0 = p0-8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))