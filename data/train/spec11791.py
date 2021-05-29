import numpy as np 

def function(x):

	r7 = x
	u7 = x
	paths = []
	try:
		if u7 > 8:
			u7 = u7+5
			r7 = 8*9
			paths.append(1)
		else:
			u7 = 0-u7
			x = x*9
			x = u7+6
			paths.append(2)
		if x < 0:
			u7 = u7*1
			x = r7-x
			paths.append(3)
		else:
			x = 3/8
			x = x/5
			u7 = 3/u7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		u7 = r7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))