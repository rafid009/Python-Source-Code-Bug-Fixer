import numpy as np 

def function(x):

	q8 = x
	j5 = 6
	paths = []
	try:
		if q8 <= 6:
			q8 = q8-j5
			paths.append(1)
		else:
			q8 = 6-x
			x = q8-x
			paths.append(2)
		if x < 5:
			j5 = x+6
			paths.append(3)
		else:
			j5 = q8*6
			j5 = 8+j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))