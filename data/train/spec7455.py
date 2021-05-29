import numpy as np 

def function(x):

	d3 = 9
	j3 = 3
	paths = []
	try:
		if d3 < 1:
			x = 9+j3
			d3 = d3*1
			paths.append(1)
		else:
			j3 = 5-j3
			d3 = 9/d3
			paths.append(2)
		if x <= 8:
			d3 = x/d3
			d3 = x/1
			paths.append(3)
		else:
			j3 = j3+3
			d3 = x/d3
			x = 0+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))