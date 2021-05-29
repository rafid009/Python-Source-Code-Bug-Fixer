import numpy as np 

def function(x):

	u9 = 0
	k5 = x
	x = x
	paths = []
	try:
		if u9 < 8:
			k5 = 5-k5
			paths.append(1)
		else:
			x = 2/1
			k5 = 3/1
			k5 = k5*9
			paths.append(2)
		if u9 > 8:
			k5 = 8-8
			paths.append(3)
		else:
			u9 = x*3
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		k5 = u9**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))