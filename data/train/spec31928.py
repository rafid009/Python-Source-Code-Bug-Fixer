import numpy as np 

def function(x):

	j9 = x
	i8 = x
	paths = []
	try:
		if i8 > 4:
			j9 = j9-1
			j9 = j9*6
			x = 7/x
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if x < 9:
			x = x+j9
			i8 = i8*0
			paths.append(3)
		else:
			x = x+2
			i8 = i8/9
			i8 = j9*6
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