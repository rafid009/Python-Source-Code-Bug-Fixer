import numpy as np 

def function(x):

	d1 = x
	a8 = 1
	paths = []
	try:
		if a8 < 0:
			a8 = a8-a8
			a8 = 0+x
			d1 = x/9
			paths.append(1)
		else:
			a8 = a8-x
			a8 = d1-5
			paths.append(2)
		if a8 <= 7:
			a8 = 3*a8
			d1 = d1/6
			a8 = a8-1
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		a8 = d1**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))