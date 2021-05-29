import numpy as np 

def function(x):

	t2 = 8
	x9 = 6
	paths = []
	try:
		if x <= 4:
			x9 = x9-9
			paths.append(1)
		else:
			x9 = 0*x9
			t2 = 0-t2
			x = 2-x
			paths.append(2)
		if x < 2:
			x9 = x9-6
			x = x-7
			paths.append(3)
		else:
			x = x+t2
			t2 = 1*x9
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))