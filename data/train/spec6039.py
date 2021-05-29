import numpy as np 

def function(x):

	o7 = x
	f8 = x
	paths = []
	try:
		if f8 <= 2:
			f8 = 3/x
			paths.append(1)
		else:
			x = 7*x
			x = 7+2
			paths.append(2)
		if f8 > 4:
			o7 = 3+o7
			o7 = o7+0
			paths.append(3)
		else:
			f8 = 6-7
			f8 = f8/5
			x = 6-1
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		f8 = o7**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))