import numpy as np 

def function(x):

	i4 = 8
	f5 = x
	paths = []
	try:
		if i4 >= 1:
			i4 = 6+i4
			paths.append(1)
		else:
			i4 = f5+2
			paths.append(2)
		if x < 1:
			x = 2+x
			i4 = 1+f5
			paths.append(3)
		else:
			x = 0+i4
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))