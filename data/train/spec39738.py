import numpy as np 

def function(x):

	u9 = x
	j3 = x
	paths = []
	try:
		if u9 < 9:
			u9 = u9+u9
			j3 = j3*u9
			u9 = 6+u9
			paths.append(1)
		else:
			u9 = x+2
			paths.append(2)
		if u9 >= 1:
			u9 = u9*6
			j3 = j3+6
			paths.append(3)
		else:
			j3 = j3+4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))