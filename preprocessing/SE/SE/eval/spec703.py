import numpy as np 

def function(x):

	i5 = x
	t6 = 8
	paths = []
	try:
		if x >= 3:
			x = 6+0
			t6 = t6+i5
			paths.append(1)
		else:
			i5 = t6-i5
			paths.append(2)
		if x >= 8:
			i5 = i5-3
			t6 = x/5
			paths.append(3)
		else:
			t6 = 7/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))