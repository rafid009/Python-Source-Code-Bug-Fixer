import numpy as np 

def function(x):

	e3 = x
	d1 = x
	paths = []
	try:
		if e3 >= 5:
			e3 = 8+e3
			e3 = e3+x
			paths.append(1)
		else:
			x = e3*6
			x = x*4
			paths.append(2)
		if d1 <= 5:
			e3 = e3-0
			d1 = 4+d1
			e3 = 8+8
			paths.append(3)
		else:
			e3 = e3/5
			e3 = e3/5
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))