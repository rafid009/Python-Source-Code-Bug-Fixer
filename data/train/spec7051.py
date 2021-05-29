import numpy as np 

def function(x):

	r1 = 9
	t6 = 0
	x = x
	paths = []
	try:
		if x < 6:
			t6 = t6+9
			r1 = 8+r1
			r1 = x*8
			paths.append(1)
		else:
			t6 = 6+t6
			paths.append(2)
		if x <= 9:
			t6 = t6+5
			paths.append(3)
		else:
			r1 = t6*r1
			r1 = 9*8
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