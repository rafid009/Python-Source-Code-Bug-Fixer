import numpy as np 

def function(x):

	d5 = 6
	j3 = x
	paths = []
	try:
		if j3 > 6:
			x = x/j3
			paths.append(1)
		else:
			x = d5/x
			x = 4+x
			x = j3/d5
			paths.append(2)
		if x >= 2:
			d5 = d5/8
			j3 = 6-j3
			d5 = j3/j3
			paths.append(3)
		else:
			j3 = j3-1
			j3 = d5/6
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