import numpy as np 

def function(x):

	f9 = 7
	y7 = 3
	paths = []
	try:
		if y7 >= 0:
			x = x/f9
			x = x/1
			paths.append(1)
		else:
			f9 = 1-f9
			paths.append(2)
		if y7 <= 2:
			f9 = y7*4
			f9 = 2+f9
			paths.append(3)
		else:
			x = x*1
			y7 = 4/y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))