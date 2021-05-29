import numpy as np 

def function(x):

	i8 = 5
	k6 = x
	paths = []
	try:
		if x >= 2:
			i8 = 6*i8
			paths.append(1)
		else:
			x = i8/8
			paths.append(2)
		if i8 > 6:
			i8 = x/k6
			x = 4+i8
			paths.append(3)
		else:
			i8 = i8/1
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		i8 = k6**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))