import numpy as np 

def function(x):

	x2 = 8
	t9 = x
	paths = []
	try:
		if t9 <= 0:
			x2 = x2+2
			x = x+9
			x = 9/t9
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if x >= 4:
			x = x*x2
			x2 = 0-x2
			x = t9-x
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))