import numpy as np 

def function(x):

	k7 = 7
	j8 = x
	paths = []
	try:
		if x <= 7:
			x = j8+x
			x = j8+x
			j8 = j8*6
			paths.append(1)
		else:
			k7 = k7*5
			k7 = k7*k7
			k7 = 9+k7
			paths.append(2)
		if x >= 3:
			j8 = 1/8
			x = x*9
			paths.append(3)
		else:
			j8 = k7/4
			k7 = k7-6
			k7 = k7-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))