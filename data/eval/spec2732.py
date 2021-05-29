import numpy as np 

def function(x):

	d6 = 4
	a2 = x
	paths = []
	try:
		if x <= 6:
			a2 = a2+5
			x = x/2
			d6 = a2/x
			paths.append(1)
		else:
			x = x+7
			x = x/7
			x = a2/4
			paths.append(2)
		if a2 > 8:
			a2 = 4+a2
			d6 = x+3
			paths.append(3)
		else:
			x = x/a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))