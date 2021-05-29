import numpy as np 

def function(x):

	y3 = x
	j9 = 1
	paths = []
	try:
		if j9 <= 6:
			j9 = y3+j9
			x = x+4
			x = x*7
			paths.append(1)
		else:
			x = x+j9
			y3 = 1*4
			x = x-x
			paths.append(2)
		if j9 <= 1:
			x = j9/5
			j9 = j9-5
			j9 = j9+j9
			paths.append(3)
		else:
			y3 = y3*7
			x = j9*x
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		j9 = y3**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))