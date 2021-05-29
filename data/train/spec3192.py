import numpy as np 

def function(x):

	u7 = 9
	k4 = x
	paths = []
	try:
		if u7 >= 8:
			x = x/7
			u7 = k4/5
			paths.append(1)
		else:
			x = 0*0
			paths.append(2)
		if x > 9:
			x = 0/u7
			k4 = 8*6
			k4 = 0+8
			paths.append(3)
		else:
			k4 = 2-k4
			u7 = 6/x
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))