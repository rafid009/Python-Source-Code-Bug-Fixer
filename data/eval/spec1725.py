import numpy as np 

def function(x):

	r7 = 6
	t7 = x
	paths = []
	try:
		if r7 > 0:
			x = 1*x
			t7 = t7*6
			t7 = 5*t7
			paths.append(1)
		else:
			t7 = 0*9
			r7 = 2*r7
			x = 1/x
			paths.append(2)
		if x > 4:
			t7 = 8-r7
			x = 8/x
			paths.append(3)
		else:
			r7 = x/4
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