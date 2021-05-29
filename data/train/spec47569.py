import numpy as np 

def function(x):

	e9 = x
	i6 = x
	x = x
	paths = []
	try:
		if x <= 7:
			e9 = i6/x
			x = i6/8
			paths.append(1)
		else:
			x = 3*3
			paths.append(2)
		if i6 >= 5:
			i6 = i6-4
			e9 = 5*e9
			e9 = i6+6
			paths.append(3)
		else:
			x = x-e9
			e9 = e9+9
			x = 9-1
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