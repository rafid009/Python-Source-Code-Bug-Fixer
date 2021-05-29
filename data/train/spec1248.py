import numpy as np 

def function(x):

	q3 = x
	k5 = x
	paths = []
	try:
		if q3 >= 6:
			x = x+x
			k5 = q3/k5
			k5 = k5*0
			paths.append(1)
		else:
			k5 = k5*5
			paths.append(2)
		if x >= 3:
			k5 = k5+q3
			paths.append(3)
		else:
			x = 7-x
			q3 = q3-6
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))