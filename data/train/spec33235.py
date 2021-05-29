import numpy as np 

def function(x):

	d6 = x
	d7 = 5
	paths = []
	try:
		if x < 8:
			x = 5-3
			x = d7*d7
			d7 = d7-x
			paths.append(1)
		else:
			x = x+0
			d6 = d6+d7
			paths.append(2)
		if d6 <= 5:
			d7 = 0/d7
			x = x-1
			paths.append(3)
		else:
			x = 4*x
			x = x+9
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))