import numpy as np 

def function(x):

	j8 = x
	f1 = x
	paths = []
	try:
		if j8 <= 8:
			f1 = 7/f1
			paths.append(1)
		else:
			f1 = f1-4
			j8 = j8*j8
			x = x/8
			paths.append(2)
		if x <= 3:
			f1 = f1+f1
			f1 = f1/j8
			f1 = f1*f1
			paths.append(3)
		else:
			x = 9+6
			x = 0+x
			j8 = j8/j8
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