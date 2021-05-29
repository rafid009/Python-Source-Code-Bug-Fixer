import numpy as np 

def function(x):

	j9 = 9
	j4 = x
	paths = []
	try:
		if j4 >= 8:
			j9 = 5-j9
			j4 = x/x
			paths.append(1)
		else:
			j4 = x*1
			j4 = x+9
			x = x/x
			paths.append(2)
		if j4 > 6:
			j4 = x-j4
			x = x*5
			j4 = j4*4
			paths.append(3)
		else:
			x = 6-j4
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))