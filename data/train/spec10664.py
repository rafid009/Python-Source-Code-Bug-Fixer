import numpy as np 

def function(x):

	j8 = 9
	y9 = 9
	paths = []
	try:
		if y9 <= 2:
			j8 = j8+8
			paths.append(1)
		else:
			j8 = j8*j8
			x = 1-x
			paths.append(2)
		if j8 <= 0:
			x = 1*x
			j8 = x/j8
			x = x+1
			paths.append(3)
		else:
			j8 = j8*5
			j8 = 9*j8
			j8 = 5-j8
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))