import numpy as np 

def function(x):

	t4 = 2
	t3 = 8
	paths = []
	try:
		if x >= 4:
			x = 0+9
			paths.append(1)
		else:
			t4 = 0-8
			x = x/5
			paths.append(2)
		if x > 7:
			t3 = 8+t3
			t3 = t3-4
			t3 = 6/4
			paths.append(3)
		else:
			t3 = t3*8
			t3 = t3-5
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