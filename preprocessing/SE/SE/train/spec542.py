import numpy as np 

def function(x):

	t6 = 5
	d6 = 1
	paths = []
	try:
		if t6 < 5:
			t6 = 8*t6
			x = d6/2
			d6 = d6+9
			paths.append(1)
		else:
			d6 = x/1
			paths.append(2)
		if t6 < 7:
			x = 9-x
			x = 5+x
			paths.append(3)
		else:
			x = 1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))