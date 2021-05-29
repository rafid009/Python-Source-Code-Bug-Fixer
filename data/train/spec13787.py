import numpy as np 

def function(x):

	q0 = x
	d3 = 1
	paths = []
	try:
		if d3 < 5:
			d3 = 1/d3
			d3 = 2+d3
			paths.append(1)
		else:
			x = x+2
			x = x/5
			d3 = 4-d3
			paths.append(2)
		if x > 7:
			x = 2/x
			x = q0*0
			q0 = 0-x
			paths.append(3)
		else:
			q0 = q0-9
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		d3 = q0**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))