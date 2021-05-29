import numpy as np 

def function(x):

	t3 = 8
	z4 = x
	paths = []
	try:
		if z4 < 2:
			z4 = z4/9
			t3 = t3/6
			paths.append(1)
		else:
			t3 = t3*5
			z4 = z4+9
			paths.append(2)
		if x >= 8:
			t3 = x+3
			t3 = t3/3
			x = x/5
			paths.append(3)
		else:
			t3 = t3/6
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))