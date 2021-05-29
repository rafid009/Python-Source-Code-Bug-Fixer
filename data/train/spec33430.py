import numpy as np 

def function(x):

	j8 = x
	y8 = 5
	paths = []
	try:
		if j8 <= 9:
			x = 1+2
			x = 7/x
			y8 = j8-y8
			paths.append(1)
		else:
			j8 = j8-2
			j8 = j8/4
			x = x-j8
			paths.append(2)
		if x < 8:
			x = x/7
			y8 = 3-y8
			j8 = j8+y8
			paths.append(3)
		else:
			x = 2/8
			j8 = j8*y8
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