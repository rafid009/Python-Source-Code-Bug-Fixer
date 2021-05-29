import numpy as np 

def function(x):

	p0 = x
	k6 = x
	paths = []
	try:
		if x > 8:
			x = 5/p0
			paths.append(1)
		else:
			x = 2*x
			x = 7+x
			paths.append(2)
		if x < 6:
			k6 = k6*1
			paths.append(3)
		else:
			x = x*8
			p0 = 6-p0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))