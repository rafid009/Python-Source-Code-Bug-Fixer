import numpy as np 

def function(x):

	i0 = x
	j9 = x
	paths = []
	try:
		if x < 4:
			i0 = i0+1
			j9 = 8-j9
			i0 = i0+7
			paths.append(1)
		else:
			i0 = i0*j9
			j9 = j9*7
			i0 = 1+i0
			paths.append(2)
		if x > 5:
			x = 7-i0
			paths.append(3)
		else:
			x = x-x
			x = 1-x
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))