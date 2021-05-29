import numpy as np 

def function(x):

	t8 = 5
	i5 = x
	paths = []
	try:
		if i5 <= 5:
			t8 = 3/7
			t8 = 4/x
			paths.append(1)
		else:
			x = 1/5
			paths.append(2)
		if x > 0:
			x = x/t8
			paths.append(3)
		else:
			t8 = t8+t8
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