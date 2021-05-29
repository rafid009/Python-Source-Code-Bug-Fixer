import numpy as np 

def function(x):

	r4 = 4
	t6 = x
	paths = []
	try:
		if t6 < 8:
			r4 = 5/r4
			paths.append(1)
		else:
			x = 3+r4
			x = 6*x
			paths.append(2)
		if r4 < 4:
			r4 = 3/r4
			r4 = 7/r4
			paths.append(3)
		else:
			r4 = 2/r4
			r4 = r4+3
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))