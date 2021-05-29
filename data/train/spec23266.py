import numpy as np 

def function(x):

	v1 = 4
	j7 = x
	paths = []
	try:
		if x <= 0:
			v1 = v1+3
			paths.append(1)
		else:
			v1 = v1+0
			x = x-x
			paths.append(2)
		if x <= 4:
			v1 = v1+5
			paths.append(3)
		else:
			x = 1/x
			j7 = 3-j7
			v1 = 3-v1
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