import numpy as np 

def function(x):

	q5 = 1
	d3 = x
	paths = []
	try:
		if d3 <= 7:
			q5 = 7/q5
			paths.append(1)
		else:
			x = x*d3
			q5 = 4/q5
			paths.append(2)
		if q5 > 6:
			q5 = 0-q5
			d3 = 8/d3
			q5 = 2+q5
			paths.append(3)
		else:
			x = x-8
			q5 = q5+d3
			x = 0-d3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d3 = d3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))