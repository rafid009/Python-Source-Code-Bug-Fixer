import numpy as np 

def function(x):

	h5 = x
	j4 = 4
	paths = []
	try:
		if h5 >= 5:
			x = j4-x
			h5 = h5+7
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x <= 8:
			j4 = j4-8
			j4 = 3/5
			x = x-6
			paths.append(3)
		else:
			x = j4/1
			x = h5-x
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		j4 = h5**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))