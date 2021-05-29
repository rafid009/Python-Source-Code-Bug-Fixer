import numpy as np 

def function(x):

	d3 = x
	f0 = x
	paths = []
	try:
		if f0 <= 4:
			x = x-x
			f0 = f0+x
			x = x/8
			paths.append(1)
		else:
			x = x-f0
			paths.append(2)
		if x >= 7:
			x = x*4
			paths.append(3)
		else:
			f0 = 6*x
			d3 = 3/d3
			f0 = f0*1
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		f0 = d3**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))