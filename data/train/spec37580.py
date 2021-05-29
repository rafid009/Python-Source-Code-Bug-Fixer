import numpy as np 

def function(x):

	d5 = x
	h7 = x
	paths = []
	try:
		if x > 8:
			h7 = h7/5
			paths.append(1)
		else:
			d5 = 8-d5
			d5 = h7/3
			paths.append(2)
		if x < 9:
			d5 = 7/d5
			d5 = d5+5
			x = x*h7
			paths.append(3)
		else:
			x = h7*0
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))