import numpy as np 

def function(x):

	x9 = x
	i6 = x
	paths = []
	try:
		if i6 >= 2:
			x = 0+x
			x = 1+x
			paths.append(1)
		else:
			x = 9*0
			paths.append(2)
		if i6 >= 6:
			x = 4-x
			i6 = x+x9
			paths.append(3)
		else:
			x = 6*4
			x9 = x9/3
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))