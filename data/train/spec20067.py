import numpy as np 

def function(x):

	r0 = x
	i6 = x
	paths = []
	try:
		if r0 >= 4:
			x = x+3
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x < 6:
			x = x*x
			paths.append(3)
		else:
			x = i6*x
			r0 = x-r0
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