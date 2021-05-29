import numpy as np 

def function(x):

	i5 = 3
	f8 = 4
	paths = []
	try:
		if i5 >= 8:
			f8 = f8+6
			i5 = 6-1
			i5 = i5-i5
			paths.append(1)
		else:
			x = x/6
			x = 5/x
			f8 = 3/7
			paths.append(2)
		if f8 >= 8:
			x = 9-2
			paths.append(3)
		else:
			x = x+7
			i5 = 0*9
			f8 = 2*f8
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