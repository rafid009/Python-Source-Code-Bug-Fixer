import numpy as np 

def function(x):

	o2 = x
	d5 = x
	paths = []
	try:
		if d5 > 2:
			x = o2/9
			d5 = d5/4
			o2 = x+1
			paths.append(1)
		else:
			x = 6*o2
			x = 7+x
			d5 = 0-d5
			paths.append(2)
		if d5 > 9:
			x = x*x
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))