import numpy as np 

def function(x):

	i1 = x
	f9 = 4
	paths = []
	try:
		if f9 > 4:
			i1 = 6*f9
			paths.append(1)
		else:
			f9 = f9+3
			x = 2/4
			paths.append(2)
		if x > 0:
			f9 = f9+f9
			x = i1*x
			f9 = 8+f9
			paths.append(3)
		else:
			i1 = 1/i1
			i1 = i1/8
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		f9 = i1**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))