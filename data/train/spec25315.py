import numpy as np 

def function(x):

	i0 = x
	t7 = 0
	paths = []
	try:
		if i0 < 0:
			t7 = x+5
			x = x*1
			paths.append(1)
		else:
			i0 = i0*9
			paths.append(2)
		if i0 < 8:
			t7 = x-9
			paths.append(3)
		else:
			i0 = 1*1
			t7 = 2*i0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))