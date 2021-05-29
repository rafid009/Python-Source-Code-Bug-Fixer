import numpy as np 

def function(x):

	d3 = 0
	k1 = 1
	paths = []
	try:
		if k1 <= 4:
			k1 = x*k1
			paths.append(1)
		else:
			k1 = 9-k1
			paths.append(2)
		if k1 > 9:
			d3 = x/x
			x = x+k1
			x = x/x
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		d3 = k1**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))