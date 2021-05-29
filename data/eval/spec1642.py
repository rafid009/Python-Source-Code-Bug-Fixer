import numpy as np 

def function(x):

	r9 = x
	t1 = 2
	paths = []
	try:
		if t1 <= 1:
			x = 6+5
			r9 = 9*r9
			paths.append(1)
		else:
			r9 = r9*7
			paths.append(2)
		if t1 <= 5:
			r9 = r9-5
			x = 9+x
			paths.append(3)
		else:
			r9 = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))