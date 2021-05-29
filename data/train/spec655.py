import numpy as np 

def function(x):

	t2 = x
	x3 = x
	paths = []
	try:
		if x3 < 6:
			x3 = x3-7
			paths.append(1)
		else:
			x = 5*x
			x3 = x3*6
			x = 1+x
			paths.append(2)
		if x > 5:
			t2 = t2*x
			paths.append(3)
		else:
			t2 = t2+1
			t2 = 4/t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))