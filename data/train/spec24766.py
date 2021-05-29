import numpy as np 

def function(x):

	i7 = x
	r8 = x
	paths = []
	try:
		if i7 <= 6:
			x = x*x
			r8 = 6/1
			paths.append(1)
		else:
			x = 4/x
			x = 6-x
			r8 = 8-r8
			paths.append(2)
		if i7 <= 6:
			x = x*x
			x = x+r8
			x = x+1
			paths.append(3)
		else:
			x = 7+5
			x = i7/r8
			x = r8+x
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