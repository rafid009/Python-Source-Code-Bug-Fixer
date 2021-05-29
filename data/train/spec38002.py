import numpy as np 

def function(x):

	k7 = 1
	d3 = x
	x = 6
	paths = []
	try:
		if d3 < 9:
			k7 = d3-3
			k7 = k7/k7
			x = d3/5
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if x > 5:
			k7 = 4/1
			paths.append(3)
		else:
			d3 = 5*d3
			k7 = k7-k7
			x = 6+0
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		k7 = d3**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))