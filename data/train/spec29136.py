import numpy as np 

def function(x):

	d9 = x
	j0 = x
	paths = []
	try:
		if x <= 1:
			j0 = j0*j0
			d9 = d9*d9
			paths.append(1)
		else:
			d9 = 0*0
			x = 4+x
			j0 = j0+x
			paths.append(2)
		if d9 > 2:
			x = x-7
			paths.append(3)
		else:
			x = 8/3
			x = x-5
			j0 = j0/j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))