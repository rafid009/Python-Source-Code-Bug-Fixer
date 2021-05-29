import numpy as np 

def function(x):

	t2 = 3
	y5 = x
	paths = []
	try:
		if t2 < 6:
			y5 = x/x
			y5 = 5/y5
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if y5 <= 7:
			t2 = y5/5
			paths.append(3)
		else:
			x = y5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))