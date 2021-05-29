import numpy as np 

def function(x):

	j4 = x
	x6 = 9
	paths = []
	try:
		if x6 >= 9:
			x = x*x
			x = x-5
			paths.append(1)
		else:
			j4 = 3-j4
			paths.append(2)
		if j4 < 4:
			x6 = x6/5
			x6 = 7+x6
			paths.append(3)
		else:
			x = 5-x
			x6 = x6-x
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