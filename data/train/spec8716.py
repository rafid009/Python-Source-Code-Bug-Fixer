import numpy as np 

def function(x):

	j4 = 1
	d9 = x
	paths = []
	try:
		if d9 > 0:
			x = d9-d9
			d9 = 1-j4
			paths.append(1)
		else:
			j4 = x*j4
			paths.append(2)
		if j4 < 0:
			j4 = j4*4
			d9 = 4-d9
			d9 = 4-d9
			paths.append(3)
		else:
			x = x*7
			j4 = d9*j4
			x = 1*1
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		d9 = j4**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))