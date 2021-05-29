import numpy as np 

def function(x):

	e1 = x
	j7 = 1
	paths = []
	try:
		if e1 > 6:
			j7 = 8*6
			paths.append(1)
		else:
			j7 = j7*j7
			e1 = e1*8
			j7 = 8/j7
			paths.append(2)
		if e1 >= 4:
			j7 = j7-e1
			paths.append(3)
		else:
			j7 = 7-1
			x = 2+x
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