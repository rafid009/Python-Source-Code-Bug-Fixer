import numpy as np 

def function(x):

	d9 = 6
	t3 = 7
	paths = []
	try:
		if x > 8:
			d9 = d9*d9
			paths.append(1)
		else:
			t3 = x-0
			paths.append(2)
		if d9 > 0:
			d9 = d9/4
			paths.append(3)
		else:
			x = 2/d9
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))