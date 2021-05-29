import numpy as np 

def function(x):

	n0 = x
	t3 = 4
	paths = []
	try:
		if t3 < 8:
			x = x-t3
			x = 5/x
			paths.append(1)
		else:
			t3 = t3-t3
			x = 2+x
			paths.append(2)
		if t3 >= 4:
			t3 = n0*t3
			n0 = n0*t3
			paths.append(3)
		else:
			x = x+5
			n0 = 7*n0
			x = n0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))