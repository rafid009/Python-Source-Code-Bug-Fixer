import numpy as np 

def function(x):

	f3 = 6
	b8 = 2
	paths = []
	try:
		if x >= 0:
			b8 = 3-3
			x = x-f3
			paths.append(1)
		else:
			f3 = 7+f3
			f3 = 8/f3
			x = 8/6
			paths.append(2)
		if f3 < 9:
			b8 = 0-7
			paths.append(3)
		else:
			b8 = 8*b8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		f3 = b8**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))