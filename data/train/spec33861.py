import numpy as np 

def function(x):

	k9 = 7
	d3 = x
	paths = []
	try:
		if k9 >= 4:
			d3 = 5+x
			k9 = 6+8
			paths.append(1)
		else:
			d3 = d3*4
			paths.append(2)
		if d3 <= 6:
			x = 6/x
			paths.append(3)
		else:
			x = 9+x
			d3 = d3+7
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))