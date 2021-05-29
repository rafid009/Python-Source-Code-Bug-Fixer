import numpy as np 

def function(x):

	d0 = 1
	j7 = 3
	paths = []
	try:
		if x <= 1:
			x = x+5
			x = x-1
			d0 = 7-d0
			paths.append(1)
		else:
			x = x-x
			x = j7+2
			j7 = j7+8
			paths.append(2)
		if j7 <= 7:
			d0 = 8+d0
			d0 = 4*x
			paths.append(3)
		else:
			x = 9+3
			j7 = j7/5
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))