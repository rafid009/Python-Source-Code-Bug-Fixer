import numpy as np 

def function(x):

	t4 = 9
	x4 = 4
	paths = []
	try:
		if t4 > 8:
			x = x4*x
			x4 = x4+x4
			x4 = x*x4
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if x < 0:
			x4 = 4/x4
			t4 = t4+1
			x4 = t4-x
			paths.append(3)
		else:
			x = x/2
			t4 = 2+t4
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