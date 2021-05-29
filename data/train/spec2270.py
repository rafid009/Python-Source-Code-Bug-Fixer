import numpy as np 

def function(x):

	d8 = x
	a8 = x
	paths = []
	try:
		if d8 > 2:
			x = 6/x
			a8 = a8+d8
			paths.append(1)
		else:
			x = x/1
			x = d8-0
			paths.append(2)
		if a8 > 3:
			x = x-2
			x = x/d8
			paths.append(3)
		else:
			d8 = d8*d8
			x = 2+x
			d8 = d8-9
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))