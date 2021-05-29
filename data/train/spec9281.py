import numpy as np 

def function(x):

	d3 = 9
	q5 = x
	paths = []
	try:
		if x > 1:
			d3 = 1-9
			d3 = 5-d3
			d3 = q5/q5
			paths.append(1)
		else:
			x = q5*7
			q5 = q5+q5
			d3 = d3+3
			paths.append(2)
		if q5 > 9:
			d3 = d3+0
			d3 = 5+1
			paths.append(3)
		else:
			d3 = d3*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))