import numpy as np 

def function(x):

	f2 = x
	d3 = 6
	paths = []
	try:
		if d3 >= 4:
			x = 0+6
			f2 = f2*4
			x = x/x
			paths.append(1)
		else:
			x = d3-5
			f2 = x/f2
			d3 = d3/8
			paths.append(2)
		if d3 >= 8:
			f2 = f2-7
			x = x+x
			paths.append(3)
		else:
			d3 = f2+d3
			x = x-1
			x = 2-d3
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