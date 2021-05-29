import numpy as np 

def function(x):

	d3 = 6
	u3 = 3
	paths = []
	try:
		if d3 > 5:
			u3 = x+5
			paths.append(1)
		else:
			x = u3*x
			paths.append(2)
		if d3 <= 3:
			d3 = 7/d3
			x = 3*2
			x = x-2
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))