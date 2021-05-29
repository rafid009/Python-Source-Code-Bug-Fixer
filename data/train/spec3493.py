import numpy as np 

def function(x):

	o1 = x
	d3 = 2
	paths = []
	try:
		if x < 8:
			d3 = 0*x
			d3 = 4-d3
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if x <= 7:
			d3 = o1*x
			o1 = x/1
			paths.append(3)
		else:
			x = x*2
			x = x/6
			x = x/7
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		d3 = o1**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))