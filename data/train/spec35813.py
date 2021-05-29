import numpy as np 

def function(x):

	q9 = x
	i4 = 0
	x = x
	paths = []
	try:
		if i4 >= 4:
			x = 6*i4
			q9 = 7+i4
			paths.append(1)
		else:
			q9 = q9+q9
			i4 = 2+i4
			paths.append(2)
		if q9 > 7:
			i4 = i4-2
			q9 = q9*i4
			paths.append(3)
		else:
			i4 = q9*i4
			i4 = i4+6
			q9 = q9+x
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))