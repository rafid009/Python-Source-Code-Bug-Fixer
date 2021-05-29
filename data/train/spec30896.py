import numpy as np 

def function(x):

	i6 = x
	x5 = x
	x = x
	paths = []
	try:
		if i6 >= 7:
			i6 = 7-i6
			paths.append(1)
		else:
			x5 = 5*x5
			x = x*9
			paths.append(2)
		if i6 > 7:
			i6 = i6*3
			x = x*x5
			paths.append(3)
		else:
			i6 = i6+3
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		i6 = x5**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))