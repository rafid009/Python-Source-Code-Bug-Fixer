import numpy as np 

def function(x):

	h6 = 6
	d5 = x
	x = 8
	paths = []
	try:
		if d5 <= 5:
			x = x*0
			d5 = 1/d5
			paths.append(1)
		else:
			h6 = d5/5
			d5 = 5*d5
			x = 6/x
			paths.append(2)
		if h6 >= 7:
			h6 = 1/h6
			paths.append(3)
		else:
			h6 = h6+5
			d5 = d5+1
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