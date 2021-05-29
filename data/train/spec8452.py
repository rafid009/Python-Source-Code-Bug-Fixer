import numpy as np 

def function(x):

	p4 = x
	r7 = 2
	paths = []
	try:
		if r7 > 5:
			r7 = r7/x
			paths.append(1)
		else:
			x = 3/r7
			paths.append(2)
		if p4 < 7:
			p4 = 5+p4
			x = x/p4
			x = x+8
			paths.append(3)
		else:
			r7 = 1+1
			x = x/p4
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