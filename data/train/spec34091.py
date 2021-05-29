import numpy as np 

def function(x):

	z1 = x
	t7 = x
	x = 1
	paths = []
	try:
		if t7 > 2:
			t7 = x+x
			x = x*9
			paths.append(1)
		else:
			x = z1-z1
			x = t7+2
			paths.append(2)
		if z1 > 9:
			x = 1-t7
			paths.append(3)
		else:
			x = x*x
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))