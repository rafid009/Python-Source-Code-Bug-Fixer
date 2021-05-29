import numpy as np 

def function(x):

	u7 = x
	i5 = 3
	paths = []
	try:
		if x > 6:
			x = 5-8
			u7 = u7*i5
			paths.append(1)
		else:
			i5 = i5*6
			i5 = 3+i5
			i5 = i5+x
			paths.append(2)
		if x <= 0:
			x = i5*5
			paths.append(3)
		else:
			u7 = u7*6
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))