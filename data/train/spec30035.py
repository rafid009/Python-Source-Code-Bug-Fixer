import numpy as np 

def function(x):

	f2 = 5
	y6 = x
	paths = []
	try:
		if f2 <= 8:
			x = 5/x
			y6 = y6*9
			paths.append(1)
		else:
			y6 = 9-y6
			x = x+y6
			paths.append(2)
		if y6 < 7:
			f2 = y6+9
			x = 1+4
			paths.append(3)
		else:
			x = x/y6
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))