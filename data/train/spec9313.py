import numpy as np 

def function(x):

	v4 = 4
	p4 = x
	x = x
	paths = []
	try:
		if p4 >= 2:
			p4 = p4*v4
			v4 = v4*v4
			p4 = p4*v4
			paths.append(1)
		else:
			x = v4*x
			v4 = 6*7
			paths.append(2)
		if x < 7:
			v4 = v4-4
			x = 0*2
			x = 2-x
			paths.append(3)
		else:
			p4 = x-4
			x = x*3
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))