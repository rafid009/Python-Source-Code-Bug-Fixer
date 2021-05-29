import numpy as np 

def function(x):

	j9 = x
	j7 = x
	paths = []
	try:
		if x < 8:
			j9 = 7-j9
			j9 = 0/6
			paths.append(1)
		else:
			x = j9*4
			j9 = 2+j9
			paths.append(2)
		if x <= 9:
			j9 = j9/4
			j9 = 7/j7
			paths.append(3)
		else:
			j9 = j9-x
			j9 = x+8
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))