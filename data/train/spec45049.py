import numpy as np 

def function(x):

	j8 = 6
	u1 = 5
	paths = []
	try:
		if j8 >= 2:
			j8 = x-7
			paths.append(1)
		else:
			x = x/x
			j8 = j8+6
			paths.append(2)
		if j8 <= 1:
			x = 1/x
			j8 = j8+x
			paths.append(3)
		else:
			j8 = j8/5
			u1 = u1/u1
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		u1 = j8**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))