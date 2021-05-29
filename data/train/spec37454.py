import numpy as np 

def function(x):

	t4 = x
	d6 = 1
	paths = []
	try:
		if t4 < 3:
			x = x/d6
			paths.append(1)
		else:
			t4 = x*3
			x = 1*9
			paths.append(2)
		if t4 > 6:
			x = 1+d6
			x = 8+x
			paths.append(3)
		else:
			t4 = t4*x
			t4 = t4/x
			t4 = 4*9
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