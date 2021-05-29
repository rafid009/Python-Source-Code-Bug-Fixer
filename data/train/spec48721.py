import numpy as np 

def function(x):

	i5 = x
	f4 = x
	paths = []
	try:
		if f4 >= 9:
			f4 = f4+9
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x < 1:
			i5 = x*f4
			f4 = f4-3
			i5 = 9-i5
			paths.append(3)
		else:
			f4 = 3*x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))