import numpy as np 

def function(x):

	j4 = x
	t7 = 7
	paths = []
	try:
		if j4 > 2:
			j4 = 6-j4
			x = x/j4
			paths.append(1)
		else:
			t7 = 6*6
			paths.append(2)
		if j4 >= 3:
			t7 = 9-t7
			t7 = 0*t7
			paths.append(3)
		else:
			x = j4-0
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))