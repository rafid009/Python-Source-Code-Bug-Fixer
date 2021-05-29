import numpy as np 

def function(x):

	e2 = x
	d0 = x
	paths = []
	try:
		if e2 > 3:
			e2 = 9-e2
			e2 = 7+e2
			paths.append(1)
		else:
			e2 = d0+e2
			e2 = x/7
			paths.append(2)
		if d0 < 9:
			d0 = d0+d0
			d0 = d0/x
			x = x-8
			paths.append(3)
		else:
			x = x*2
			d0 = 2+d0
			d0 = d0-9
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))