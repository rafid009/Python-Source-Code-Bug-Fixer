import numpy as np 

def function(x):

	d3 = 6
	f2 = 8
	paths = []
	try:
		if f2 < 1:
			f2 = 4+d3
			x = 4*d3
			paths.append(1)
		else:
			f2 = 2+f2
			paths.append(2)
		if d3 < 9:
			x = x*6
			d3 = f2-x
			f2 = f2+d3
			paths.append(3)
		else:
			f2 = f2+f2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		d3 = f2**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))