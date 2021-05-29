import numpy as np 

def function(x):

	t2 = 9
	i9 = x
	paths = []
	try:
		if t2 >= 7:
			t2 = 0/2
			x = x+i9
			i9 = 8/i9
			paths.append(1)
		else:
			t2 = i9*t2
			t2 = t2-0
			paths.append(2)
		if x >= 1:
			i9 = 3+t2
			paths.append(3)
		else:
			i9 = i9*i9
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