import numpy as np 

def function(x):

	d3 = 9
	j3 = 7
	paths = []
	try:
		if j3 >= 1:
			x = 3/x
			d3 = d3-1
			paths.append(1)
		else:
			d3 = 1+d3
			x = 6+x
			d3 = 7-x
			paths.append(2)
		if x >= 6:
			d3 = 6-x
			d3 = d3*3
			paths.append(3)
		else:
			j3 = 3+j3
			j3 = j3*8
			x = x/6
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