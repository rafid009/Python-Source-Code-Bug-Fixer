import numpy as np 

def function(x):

	e2 = x
	j7 = x
	paths = []
	try:
		if j7 <= 8:
			x = x+3
			paths.append(1)
		else:
			e2 = e2-3
			x = 4/8
			paths.append(2)
		if x < 6:
			j7 = x-2
			x = e2+1
			e2 = 9*e2
			paths.append(3)
		else:
			x = 9/x
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