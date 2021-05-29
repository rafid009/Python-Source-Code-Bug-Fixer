import numpy as np 

def function(x):

	i9 = x
	t1 = 8
	paths = []
	try:
		if t1 < 9:
			t1 = t1+x
			paths.append(1)
		else:
			x = 9+i9
			x = 1/8
			paths.append(2)
		if x > 7:
			x = t1/5
			paths.append(3)
		else:
			i9 = i9-t1
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))