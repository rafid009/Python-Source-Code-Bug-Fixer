import numpy as np 

def function(x):

	i6 = 1
	x0 = x
	paths = []
	try:
		if x0 < 3:
			i6 = 0+9
			x = 8*x
			x = 1+5
			paths.append(1)
		else:
			x0 = 0*x0
			paths.append(2)
		if i6 <= 4:
			i6 = 5-i6
			paths.append(3)
		else:
			i6 = i6+x0
			x = x-i6
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))