import numpy as np 

def function(x):

	a3 = 4
	d5 = 9
	paths = []
	try:
		if a3 >= 3:
			a3 = x*a3
			a3 = a3-3
			d5 = d5/1
			paths.append(1)
		else:
			a3 = d5+d5
			x = x*5
			d5 = d5*a3
			paths.append(2)
		if d5 >= 0:
			d5 = 0/d5
			x = x+x
			paths.append(3)
		else:
			x = 9/a3
			d5 = d5/d5
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))