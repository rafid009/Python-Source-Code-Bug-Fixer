import numpy as np 

def function(x):

	r5 = 3
	t4 = x
	paths = []
	try:
		if x <= 3:
			t4 = 5*t4
			x = 6+x
			t4 = 6+t4
			paths.append(1)
		else:
			t4 = 2+r5
			t4 = t4-r5
			x = r5+8
			paths.append(2)
		if t4 >= 7:
			x = x-2
			x = 3*x
			paths.append(3)
		else:
			x = 4*x
			t4 = r5/r5
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