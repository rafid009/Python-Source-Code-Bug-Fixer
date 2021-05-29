import numpy as np 

def function(x):

	f9 = 2
	y5 = x
	x = 1
	paths = []
	try:
		if y5 <= 2:
			x = 2/9
			f9 = f9+y5
			paths.append(1)
		else:
			y5 = y5*f9
			y5 = y5+8
			paths.append(2)
		if x <= 2:
			y5 = f9+7
			y5 = y5-1
			paths.append(3)
		else:
			x = x-9
			x = x*8
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		f9 = y5**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))