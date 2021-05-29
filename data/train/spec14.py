import numpy as np 

def function(x):

	d4 = 9
	d9 = 8
	paths = []
	try:
		if x > 8:
			x = 3+d4
			d9 = d9-1
			paths.append(1)
		else:
			d9 = x*5
			d9 = d4*d9
			paths.append(2)
		if d4 <= 5:
			d9 = d9*0
			d4 = x+d9
			paths.append(3)
		else:
			d4 = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))