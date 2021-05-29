import numpy as np 

def function(x):

	u9 = 6
	j5 = x
	paths = []
	try:
		if u9 <= 3:
			x = x*j5
			u9 = 9*8
			paths.append(1)
		else:
			u9 = 7-u9
			paths.append(2)
		if u9 > 1:
			u9 = 5+9
			j5 = 8/2
			paths.append(3)
		else:
			j5 = 5-x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		u9 = j5**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))