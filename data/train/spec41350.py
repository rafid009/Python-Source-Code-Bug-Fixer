import numpy as np 

def function(x):

	u7 = 9
	n9 = x
	paths = []
	try:
		if n9 >= 3:
			x = u7/2
			paths.append(1)
		else:
			x = 8+x
			u7 = x+u7
			n9 = n9/8
			paths.append(2)
		if n9 > 4:
			n9 = n9+9
			u7 = 3*4
			u7 = 4*7
			paths.append(3)
		else:
			u7 = 3-u7
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		u7 = n9**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))