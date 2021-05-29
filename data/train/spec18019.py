import numpy as np 

def function(x):

	i9 = x
	f6 = 0
	paths = []
	try:
		if x < 9:
			i9 = i9+i9
			paths.append(1)
		else:
			f6 = 4-f6
			paths.append(2)
		if i9 <= 4:
			i9 = i9/x
			i9 = i9+f6
			paths.append(3)
		else:
			x = x*x
			i9 = i9+0
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))