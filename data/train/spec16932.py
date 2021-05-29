import numpy as np 

def function(x):

	x8 = x
	i5 = x
	paths = []
	try:
		if x8 >= 4:
			x = x8+x
			x = i5-6
			paths.append(1)
		else:
			x = x+6
			x8 = 3-x8
			x = 1+2
			paths.append(2)
		if x8 > 4:
			i5 = 3/x
			x = x/7
			paths.append(3)
		else:
			x = x-i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x8 = i5**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))