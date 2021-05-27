import numpy as np 

def function(x):

	u7 = x
	j3 = x
	paths = []
	try:
		if x <= 3:
			u7 = 9+u7
			paths.append(1)
		else:
			u7 = u7*u7
			x = x*0
			paths.append(2)
		if x <= 0:
			x = 5-u7
			u7 = j3+3
			paths.append(3)
		else:
			x = u7/x
			j3 = 0/j3
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		j3 = u7**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))