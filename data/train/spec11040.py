import numpy as np 

def function(x):

	d6 = x
	h9 = 0
	x = 5
	paths = []
	try:
		if x > 0:
			h9 = 6/6
			x = 3-6
			h9 = h9*7
			paths.append(1)
		else:
			d6 = 5-3
			x = 9/h9
			paths.append(2)
		if h9 <= 1:
			x = d6+1
			d6 = 4*0
			h9 = 4-h9
			paths.append(3)
		else:
			h9 = 7*2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))