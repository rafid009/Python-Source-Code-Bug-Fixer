import numpy as np 

def function(x):

	i8 = 8
	i6 = 6
	paths = []
	try:
		if i6 < 7:
			i6 = 2*i6
			paths.append(1)
		else:
			i8 = i6*i8
			paths.append(2)
		if x <= 5:
			x = x+9
			x = 2-i6
			i6 = 0+i6
			paths.append(3)
		else:
			i8 = i8+i8
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