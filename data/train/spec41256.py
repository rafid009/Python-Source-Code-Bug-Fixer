import numpy as np 

def function(x):

	d9 = x
	j2 = 2
	paths = []
	try:
		if d9 < 8:
			d9 = 8/d9
			j2 = 9+j2
			paths.append(1)
		else:
			d9 = 6/d9
			paths.append(2)
		if j2 < 8:
			d9 = 5*6
			j2 = d9*4
			j2 = d9+j2
			paths.append(3)
		else:
			d9 = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))