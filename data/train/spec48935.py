import numpy as np 

def function(x):

	j8 = 0
	q4 = x
	paths = []
	try:
		if q4 >= 9:
			x = 7+x
			paths.append(1)
		else:
			q4 = q4/1
			q4 = q4-3
			q4 = q4/x
			paths.append(2)
		if j8 > 3:
			q4 = x+6
			paths.append(3)
		else:
			q4 = 7+0
			j8 = j8*6
			j8 = 8/3
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