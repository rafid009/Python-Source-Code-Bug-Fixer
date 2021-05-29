import numpy as np 

def function(x):

	j4 = 9
	n4 = 1
	paths = []
	try:
		if n4 >= 3:
			n4 = n4+2
			x = 1+x
			j4 = n4-1
			paths.append(1)
		else:
			j4 = j4*j4
			n4 = 9-7
			paths.append(2)
		if j4 <= 9:
			j4 = j4/4
			x = x/3
			x = 7-8
			paths.append(3)
		else:
			n4 = 1*j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))