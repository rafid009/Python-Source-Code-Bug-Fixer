import numpy as np 

def function(x):

	x7 = 3
	j8 = x
	paths = []
	try:
		if x > 3:
			x = j8+4
			x7 = x7-j8
			paths.append(1)
		else:
			j8 = x*j8
			paths.append(2)
		if x7 >= 4:
			j8 = j8*0
			paths.append(3)
		else:
			j8 = x+j8
			j8 = j8*0
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