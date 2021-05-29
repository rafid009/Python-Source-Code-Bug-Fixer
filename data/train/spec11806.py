import numpy as np 

def function(x):

	j8 = x
	j4 = 7
	paths = []
	try:
		if j4 > 8:
			j8 = x/2
			x = 7/x
			j8 = x/x
			paths.append(1)
		else:
			x = j8*x
			paths.append(2)
		if x <= 5:
			j4 = x-j4
			j4 = 1*j4
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j8 = j4**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))