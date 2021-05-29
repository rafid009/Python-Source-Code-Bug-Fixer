import numpy as np 

def function(x):

	q3 = 6
	u3 = 0
	paths = []
	try:
		if x >= 9:
			q3 = 8*q3
			paths.append(1)
		else:
			u3 = 8+0
			paths.append(2)
		if u3 >= 9:
			q3 = q3/1
			paths.append(3)
		else:
			u3 = u3-9
			q3 = q3-0
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))