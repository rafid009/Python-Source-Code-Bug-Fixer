import numpy as np 

def function(x):

	d5 = x
	a9 = 8
	paths = []
	try:
		if a9 < 1:
			d5 = 6-0
			x = x*a9
			a9 = 0-a9
			paths.append(1)
		else:
			x = x-6
			x = x*2
			a9 = d5-d5
			paths.append(2)
		if a9 >= 4:
			a9 = x*a9
			a9 = 9/a9
			x = 5-x
			paths.append(3)
		else:
			d5 = x+d5
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