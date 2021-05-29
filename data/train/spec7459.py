import numpy as np 

def function(x):

	w8 = 9
	u9 = x
	paths = []
	try:
		if x < 8:
			w8 = 7/w8
			paths.append(1)
		else:
			w8 = w8+7
			w8 = 7*x
			w8 = 0+w8
			paths.append(2)
		if x > 0:
			u9 = 6-9
			u9 = 5/u9
			u9 = w8/u9
			paths.append(3)
		else:
			w8 = 7/8
			w8 = w8-7
			x = 5+0
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