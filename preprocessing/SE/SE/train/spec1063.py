import numpy as np 

def function(x):

	j2 = 1
	u7 = 7
	paths = []
	try:
		if u7 >= 4:
			x = 9/x
			u7 = 1/x
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if j2 < 3:
			j2 = 1/4
			paths.append(3)
		else:
			j2 = j2-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))