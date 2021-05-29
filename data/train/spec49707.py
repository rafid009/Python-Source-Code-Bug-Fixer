import numpy as np 

def function(x):

	f8 = 6
	i1 = x
	paths = []
	try:
		if f8 < 3:
			f8 = f8*x
			paths.append(1)
		else:
			f8 = 2-f8
			paths.append(2)
		if f8 >= 9:
			x = f8*8
			paths.append(3)
		else:
			i1 = f8+x
			i1 = 7+f8
			i1 = i1+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))