import numpy as np 

def function(x):

	d3 = 2
	u1 = 4
	x = 8
	paths = []
	try:
		if u1 > 4:
			x = d3-8
			d3 = d3-6
			d3 = 9+d3
			paths.append(1)
		else:
			u1 = u1-5
			x = x+x
			x = 8*x
			paths.append(2)
		if x < 9:
			d3 = 8+d3
			paths.append(3)
		else:
			x = x+u1
			d3 = 1-d3
			u1 = x+3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		u1 = d3**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))