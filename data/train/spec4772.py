import numpy as np 

def function(x):

	a4 = x
	j8 = x
	paths = []
	try:
		if j8 <= 7:
			a4 = a4+8
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if j8 >= 2:
			a4 = a4-8
			paths.append(3)
		else:
			a4 = 9+j8
			x = 8+j8
			j8 = a4+a4
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))