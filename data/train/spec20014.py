import numpy as np 

def function(x):

	u9 = 2
	w6 = x
	x = x
	paths = []
	try:
		if x <= 7:
			u9 = w6+2
			x = 8-x
			u9 = x+x
			paths.append(1)
		else:
			u9 = u9+5
			u9 = 7*u9
			w6 = w6-9
			paths.append(2)
		if x >= 4:
			u9 = 8/u9
			paths.append(3)
		else:
			u9 = 5-u9
			x = x*w6
			x = 1/w6
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))