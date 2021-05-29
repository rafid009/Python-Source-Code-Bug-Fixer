import numpy as np 

def function(x):

	u6 = 9
	f6 = 4
	paths = []
	try:
		if f6 > 2:
			f6 = f6+1
			f6 = f6/2
			paths.append(1)
		else:
			x = 8*9
			x = 4+f6
			paths.append(2)
		if f6 >= 7:
			f6 = f6/x
			f6 = f6-6
			f6 = 7+f6
			paths.append(3)
		else:
			u6 = 6+f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))