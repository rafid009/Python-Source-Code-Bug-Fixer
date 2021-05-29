import numpy as np 

def function(x):

	k7 = 5
	j8 = 1
	paths = []
	try:
		if j8 >= 1:
			k7 = 2+8
			k7 = k7-k7
			paths.append(1)
		else:
			j8 = 9*x
			paths.append(2)
		if j8 > 8:
			k7 = 5+k7
			paths.append(3)
		else:
			j8 = j8*2
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))