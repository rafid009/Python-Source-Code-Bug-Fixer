import numpy as np 

def function(x):

	d9 = x
	d2 = 1
	paths = []
	try:
		if d9 <= 4:
			d9 = d9/d9
			d2 = d2/d9
			d2 = 0*7
			paths.append(1)
		else:
			x = x-x
			d9 = d9-3
			paths.append(2)
		if d9 <= 9:
			d9 = d2+d9
			d2 = x/4
			d2 = d2-3
			paths.append(3)
		else:
			d9 = 4+d2
			d9 = d9-8
			x = x-x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d2 = d9**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))