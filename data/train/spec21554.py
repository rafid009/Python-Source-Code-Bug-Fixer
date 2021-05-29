import numpy as np 

def function(x):

	j4 = x
	u5 = 1
	paths = []
	try:
		if j4 < 0:
			u5 = 5*8
			j4 = j4+4
			paths.append(1)
		else:
			u5 = u5/7
			paths.append(2)
		if j4 >= 7:
			j4 = j4-4
			u5 = u5-j4
			paths.append(3)
		else:
			x = 0-2
			x = 4-u5
			x = x*3
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		j4 = u5**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))