import numpy as np 

def function(x):

	j2 = x
	d3 = x
	paths = []
	try:
		if d3 > 3:
			j2 = 2/3
			paths.append(1)
		else:
			d3 = d3*0
			d3 = d3-7
			j2 = x*d3
			paths.append(2)
		if d3 > 7:
			x = 9-5
			d3 = 5*8
			x = 8*5
			paths.append(3)
		else:
			d3 = 3/d3
			d3 = d3+x
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