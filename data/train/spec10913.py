import numpy as np 

def function(x):

	v3 = 1
	t4 = x
	paths = []
	try:
		if x > 9:
			v3 = 6*5
			x = 6+x
			paths.append(1)
		else:
			x = x+0
			x = 0-x
			paths.append(2)
		if t4 <= 5:
			t4 = 1/v3
			paths.append(3)
		else:
			v3 = 2*v3
			v3 = v3-t4
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