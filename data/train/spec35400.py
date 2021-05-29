import numpy as np 

def function(x):

	q4 = 7
	v9 = x
	paths = []
	try:
		if x <= 0:
			x = v9+1
			paths.append(1)
		else:
			x = 2/x
			v9 = v9+1
			paths.append(2)
		if q4 <= 1:
			q4 = q4-q4
			x = 3/7
			q4 = q4-1
			paths.append(3)
		else:
			q4 = v9-q4
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))