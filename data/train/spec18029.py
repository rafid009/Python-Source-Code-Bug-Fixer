import numpy as np 

def function(x):

	i6 = 3
	q9 = x
	paths = []
	try:
		if x < 0:
			i6 = i6/i6
			i6 = i6-i6
			q9 = x-7
			paths.append(1)
		else:
			x = 0-i6
			q9 = 6/i6
			paths.append(2)
		if q9 < 4:
			q9 = q9-5
			i6 = 9-i6
			paths.append(3)
		else:
			q9 = q9+0
			i6 = 9*i6
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))