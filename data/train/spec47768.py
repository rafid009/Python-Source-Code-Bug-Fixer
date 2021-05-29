import numpy as np 

def function(x):

	k1 = 0
	u7 = 9
	paths = []
	try:
		if k1 < 5:
			k1 = 3/8
			x = x*u7
			paths.append(1)
		else:
			x = u7/3
			u7 = u7+k1
			x = 0*2
			paths.append(2)
		if u7 < 2:
			k1 = k1+x
			k1 = 7-k1
			k1 = 2+x
			paths.append(3)
		else:
			u7 = k1*u7
			u7 = 3-u7
			k1 = k1*x
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