import numpy as np 

def function(x):

	k7 = x
	i6 = x
	paths = []
	try:
		if x < 9:
			k7 = 5*x
			paths.append(1)
		else:
			i6 = i6/x
			x = 6+x
			i6 = k7*k7
			paths.append(2)
		if k7 <= 2:
			x = x/1
			i6 = i6-6
			paths.append(3)
		else:
			k7 = k7/k7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))