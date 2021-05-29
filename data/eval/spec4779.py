import numpy as np 

def function(x):

	b5 = 1
	j8 = x
	paths = []
	try:
		if j8 > 5:
			b5 = b5/j8
			j8 = j8/x
			paths.append(1)
		else:
			j8 = 6+4
			x = j8/6
			paths.append(2)
		if j8 >= 6:
			j8 = 8-j8
			x = 9+4
			paths.append(3)
		else:
			b5 = b5*9
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		b5 = j8**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))