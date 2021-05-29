import numpy as np 

def function(x):

	d3 = x
	k9 = x
	x = 7
	paths = []
	try:
		if x > 8:
			k9 = x+2
			x = x/6
			paths.append(1)
		else:
			k9 = 3-k9
			paths.append(2)
		if d3 > 4:
			k9 = 0+8
			x = x-3
			k9 = d3*x
			paths.append(3)
		else:
			x = 3*x
			k9 = k9/k9
			k9 = 5*k9
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