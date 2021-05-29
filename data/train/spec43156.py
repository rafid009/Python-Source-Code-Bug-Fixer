import numpy as np 

def function(x):

	j8 = 6
	l3 = x
	paths = []
	try:
		if j8 < 3:
			j8 = j8+2
			paths.append(1)
		else:
			l3 = 4-3
			l3 = j8+l3
			paths.append(2)
		if j8 > 1:
			x = x/6
			j8 = 4-j8
			paths.append(3)
		else:
			j8 = j8-l3
			j8 = j8+8
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