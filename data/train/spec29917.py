import numpy as np 

def function(x):

	i6 = x
	q4 = x
	paths = []
	try:
		if i6 >= 6:
			x = x+7
			x = i6/x
			paths.append(1)
		else:
			q4 = 9*4
			x = x*2
			paths.append(2)
		if q4 >= 4:
			i6 = q4/i6
			i6 = i6+7
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		q4 = i6**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))