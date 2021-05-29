import numpy as np 

def function(x):

	r8 = 9
	i9 = x
	paths = []
	try:
		if i9 <= 2:
			r8 = r8+5
			paths.append(1)
		else:
			x = x/x
			r8 = 9+1
			paths.append(2)
		if i9 <= 6:
			x = 0+x
			paths.append(3)
		else:
			x = 1-i9
			i9 = 1/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))