import numpy as np 

def function(x):

	i6 = x
	a5 = x
	paths = []
	try:
		if x > 5:
			i6 = 7*i6
			paths.append(1)
		else:
			i6 = i6*i6
			paths.append(2)
		if i6 >= 9:
			i6 = i6*a5
			a5 = 4*a5
			paths.append(3)
		else:
			i6 = x-0
			x = 4/x
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