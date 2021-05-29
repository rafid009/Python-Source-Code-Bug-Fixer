import numpy as np 

def function(x):

	j8 = 8
	n7 = x
	paths = []
	try:
		if j8 > 8:
			n7 = 8/7
			x = 8+x
			x = 4/x
			paths.append(1)
		else:
			j8 = 3*8
			j8 = j8*7
			j8 = 2-j8
			paths.append(2)
		if j8 < 4:
			x = 7+x
			paths.append(3)
		else:
			j8 = j8+n7
			x = x*4
			x = j8-x
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		j8 = n7**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))