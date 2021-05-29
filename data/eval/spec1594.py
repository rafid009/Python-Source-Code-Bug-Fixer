import numpy as np 

def function(x):

	n0 = 0
	j7 = x
	paths = []
	try:
		if x <= 6:
			j7 = j7-2
			j7 = 8/j7
			paths.append(1)
		else:
			j7 = j7*7
			paths.append(2)
		if j7 <= 3:
			j7 = j7+0
			paths.append(3)
		else:
			n0 = n0*2
			x = x+0
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