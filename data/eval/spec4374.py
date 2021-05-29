import numpy as np 

def function(x):

	p9 = x
	d0 = 3
	paths = []
	try:
		if d0 <= 5:
			p9 = p9-2
			x = x+9
			x = x-d0
			paths.append(1)
		else:
			p9 = 2-2
			p9 = 2/1
			d0 = 8+d0
			paths.append(2)
		if p9 <= 1:
			p9 = 6*2
			x = 8/1
			d0 = 0*d0
			paths.append(3)
		else:
			x = 6-x
			d0 = d0+3
			x = 3/x
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