import numpy as np 

def function(x):

	j8 = x
	n9 = 4
	paths = []
	try:
		if n9 > 2:
			j8 = 9/j8
			n9 = x/1
			x = 8+x
			paths.append(1)
		else:
			x = n9+n9
			x = n9-7
			paths.append(2)
		if x > 3:
			n9 = x-n9
			n9 = 0/4
			x = x/3
			paths.append(3)
		else:
			x = 0-9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		j8 = n9**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))