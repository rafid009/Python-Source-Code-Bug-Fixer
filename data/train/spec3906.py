import numpy as np 

def function(x):

	i5 = x
	f6 = 6
	paths = []
	try:
		if i5 <= 1:
			i5 = i5+i5
			f6 = f6*6
			paths.append(1)
		else:
			f6 = f6+0
			paths.append(2)
		if f6 < 7:
			f6 = 6-0
			x = x-x
			i5 = f6-i5
			paths.append(3)
		else:
			x = 3*x
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