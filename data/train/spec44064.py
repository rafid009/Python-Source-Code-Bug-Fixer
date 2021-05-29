import numpy as np 

def function(x):

	f6 = x
	a6 = 8
	paths = []
	try:
		if a6 < 7:
			x = x-8
			paths.append(1)
		else:
			x = x-7
			f6 = a6+f6
			paths.append(2)
		if a6 >= 3:
			f6 = 8+x
			paths.append(3)
		else:
			f6 = x/f6
			a6 = a6-x
			f6 = f6-3
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))