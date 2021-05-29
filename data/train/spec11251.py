import numpy as np 

def function(x):

	j4 = 5
	b0 = x
	paths = []
	try:
		if x > 3:
			b0 = 4+b0
			b0 = b0+6
			paths.append(1)
		else:
			x = x/j4
			x = 7/x
			paths.append(2)
		if x < 0:
			j4 = j4-0
			x = x*8
			paths.append(3)
		else:
			j4 = 9+8
			b0 = b0/x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		j4 = b0**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))