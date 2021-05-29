import numpy as np 

def function(x):

	f9 = x
	i6 = x
	paths = []
	try:
		if x > 3:
			x = 6*x
			i6 = 4-i6
			paths.append(1)
		else:
			i6 = 2/i6
			paths.append(2)
		if x >= 9:
			x = x-5
			x = f9-x
			paths.append(3)
		else:
			x = f9-2
			x = 8*i6
			i6 = i6-8
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		i6 = f9**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))