import numpy as np 

def function(x):

	r9 = 5
	p0 = x
	paths = []
	try:
		if r9 >= 4:
			r9 = r9*4
			x = x/2
			p0 = p0-8
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x < 5:
			r9 = 6-r9
			r9 = x+r9
			r9 = x-3
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))