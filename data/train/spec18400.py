import numpy as np 

def function(x):

	j8 = x
	i0 = 1
	paths = []
	try:
		if i0 > 6:
			i0 = 0-5
			i0 = 7/8
			paths.append(1)
		else:
			i0 = 5+2
			i0 = 9*j8
			paths.append(2)
		if x > 1:
			i0 = i0/1
			paths.append(3)
		else:
			x = x/i0
			i0 = 5-i0
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