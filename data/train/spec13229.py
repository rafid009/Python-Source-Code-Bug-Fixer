import numpy as np 

def function(x):

	u1 = x
	j7 = x
	paths = []
	try:
		if x < 4:
			j7 = x+1
			paths.append(1)
		else:
			j7 = 9/u1
			paths.append(2)
		if u1 > 4:
			u1 = 3/x
			j7 = 3/j7
			paths.append(3)
		else:
			u1 = u1*4
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