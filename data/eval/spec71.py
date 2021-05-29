import numpy as np 

def function(x):

	k6 = x
	j4 = 8
	paths = []
	try:
		if x < 4:
			j4 = 4+1
			k6 = 6+k6
			paths.append(1)
		else:
			j4 = 2-5
			x = x-0
			paths.append(2)
		if k6 > 6:
			x = 6-7
			j4 = 6/j4
			x = 1-x
			paths.append(3)
		else:
			j4 = 9+j4
			x = 1+k6
			j4 = 7-x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		k6 = j4**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))