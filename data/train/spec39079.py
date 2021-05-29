import numpy as np 

def function(x):

	j4 = 4
	u5 = x
	x = x
	paths = []
	try:
		if j4 > 5:
			j4 = 0+j4
			x = 1+u5
			u5 = u5+j4
			paths.append(1)
		else:
			j4 = 6*j4
			j4 = 6-j4
			paths.append(2)
		if u5 > 3:
			x = 2*u5
			j4 = 7/7
			paths.append(3)
		else:
			x = 5/x
			u5 = u5*1
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		u5 = j4**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))