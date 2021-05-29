import numpy as np 

def function(x):

	l0 = 5
	p0 = x
	paths = []
	try:
		if x > 9:
			x = 3+8
			l0 = 5-l0
			l0 = l0+1
			paths.append(1)
		else:
			p0 = p0*3
			paths.append(2)
		if l0 < 5:
			l0 = l0*8
			l0 = l0*l0
			l0 = 6/l0
			paths.append(3)
		else:
			l0 = l0*p0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))