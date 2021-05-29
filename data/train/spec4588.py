import numpy as np 

def function(x):

	d9 = x
	h2 = 2
	paths = []
	try:
		if h2 >= 3:
			h2 = 3*3
			paths.append(1)
		else:
			h2 = 3+h2
			x = 4-h2
			x = x/1
			paths.append(2)
		if x <= 4:
			h2 = h2/1
			d9 = d9/x
			x = 1*x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))