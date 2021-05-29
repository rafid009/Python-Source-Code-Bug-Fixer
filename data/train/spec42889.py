import numpy as np 

def function(x):

	j7 = 3
	v4 = 7
	paths = []
	try:
		if x >= 5:
			j7 = j7/3
			x = 4*v4
			paths.append(1)
		else:
			j7 = j7-v4
			x = x+x
			j7 = 1+j7
			paths.append(2)
		if x > 6:
			j7 = 6-j7
			v4 = v4*7
			paths.append(3)
		else:
			v4 = 8*v4
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