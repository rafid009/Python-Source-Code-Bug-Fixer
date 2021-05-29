import numpy as np 

def function(x):

	n4 = 4
	t1 = 8
	paths = []
	try:
		if x < 2:
			n4 = x*n4
			t1 = t1-6
			x = x+3
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if t1 <= 3:
			n4 = n4+x
			x = 2+x
			paths.append(3)
		else:
			x = 1+3
			x = x/7
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