import numpy as np 

def function(x):

	r8 = x
	i8 = 2
	paths = []
	try:
		if r8 <= 1:
			r8 = 1-r8
			paths.append(1)
		else:
			i8 = i8+1
			r8 = 1*r8
			paths.append(2)
		if r8 <= 3:
			x = 8/i8
			r8 = 1+r8
			paths.append(3)
		else:
			r8 = r8/9
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