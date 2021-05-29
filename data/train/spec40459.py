import numpy as np 

def function(x):

	j8 = 5
	n8 = 7
	paths = []
	try:
		if n8 >= 8:
			x = x*7
			j8 = 2-8
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if x > 2:
			n8 = n8*6
			paths.append(3)
		else:
			x = 2/6
			j8 = 5+j8
			n8 = 4-5
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		j8 = n8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))