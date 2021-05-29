import numpy as np 

def function(x):

	a8 = 5
	d7 = x
	paths = []
	try:
		if x > 7:
			a8 = 7/a8
			a8 = 7-a8
			paths.append(1)
		else:
			a8 = 3+x
			a8 = 2+d7
			x = 5*x
			paths.append(2)
		if d7 <= 5:
			a8 = d7-d7
			d7 = 4-d7
			x = x/9
			paths.append(3)
		else:
			x = x-d7
			a8 = a8+a8
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))