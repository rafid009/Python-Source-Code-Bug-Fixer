import numpy as np 

def function(x):

	p1 = 7
	f5 = x
	paths = []
	try:
		if f5 > 1:
			p1 = 0*8
			paths.append(1)
		else:
			f5 = f5*4
			paths.append(2)
		if p1 < 0:
			f5 = 7+f5
			x = 4+x
			paths.append(3)
		else:
			f5 = p1+6
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