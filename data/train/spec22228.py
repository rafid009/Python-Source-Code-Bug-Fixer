import numpy as np 

def function(x):

	w9 = 6
	i4 = 5
	paths = []
	try:
		if x > 4:
			x = x+5
			x = 8-x
			x = x*1
			paths.append(1)
		else:
			i4 = i4*1
			paths.append(2)
		if x >= 8:
			x = x/7
			x = 2*x
			x = 2*x
			paths.append(3)
		else:
			x = 0+x
			i4 = 9+w9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))