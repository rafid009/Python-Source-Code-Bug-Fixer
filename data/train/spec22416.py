import numpy as np 

def function(x):

	r2 = x
	j2 = x
	paths = []
	try:
		if r2 >= 1:
			j2 = 2/6
			x = x+j2
			paths.append(1)
		else:
			r2 = 4/j2
			r2 = r2+2
			paths.append(2)
		if j2 < 8:
			r2 = 0-r2
			x = x-r2
			paths.append(3)
		else:
			j2 = 9/j2
			j2 = j2*7
			j2 = 3/7
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))