import numpy as np 

def function(x):

	x9 = 3
	k6 = 6
	paths = []
	try:
		if x9 < 3:
			x = x/8
			paths.append(1)
		else:
			x9 = x9*4
			x = 2-x9
			x = 7/7
			paths.append(2)
		if x9 > 7:
			k6 = 4-6
			x9 = x9*0
			paths.append(3)
		else:
			k6 = k6/x9
			x = 3+9
			k6 = k6-6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x9 = k6**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))