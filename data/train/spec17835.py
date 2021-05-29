import numpy as np 

def function(x):

	j3 = 7
	t1 = 7
	paths = []
	try:
		if x > 7:
			j3 = j3+6
			paths.append(1)
		else:
			t1 = t1/3
			t1 = x/t1
			paths.append(2)
		if x < 6:
			x = x/j3
			paths.append(3)
		else:
			t1 = t1/3
			x = 1-8
			x = x/4
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