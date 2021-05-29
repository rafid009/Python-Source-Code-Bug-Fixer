import numpy as np 

def function(x):

	u9 = x
	j4 = 4
	paths = []
	try:
		if u9 >= 3:
			x = x/7
			j4 = 9/2
			j4 = 7+j4
			paths.append(1)
		else:
			j4 = 7-x
			u9 = 0-u9
			paths.append(2)
		if u9 > 2:
			u9 = u9/4
			paths.append(3)
		else:
			u9 = 9*x
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		j4 = u9**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))