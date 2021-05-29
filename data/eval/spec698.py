import numpy as np 

def function(x):

	j9 = 3
	f8 = x
	paths = []
	try:
		if j9 > 3:
			f8 = 1/f8
			x = x-3
			x = f8/x
			paths.append(1)
		else:
			j9 = 6-7
			f8 = 3*f8
			paths.append(2)
		if j9 > 1:
			j9 = 4/j9
			j9 = 1/j9
			paths.append(3)
		else:
			x = 8/f8
			f8 = 5/8
			x = 4*f8
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		f8 = j9**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))