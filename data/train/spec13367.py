import numpy as np 

def function(x):

	f7 = 8
	k6 = 6
	paths = []
	try:
		if x > 2:
			f7 = 7/f7
			x = x/9
			f7 = 0/x
			paths.append(1)
		else:
			k6 = k6-3
			x = 9-x
			f7 = 8/f7
			paths.append(2)
		if f7 <= 1:
			k6 = k6*4
			f7 = x-3
			x = 9-x
			paths.append(3)
		else:
			f7 = f7*f7
			k6 = 3-k6
			f7 = 9*3
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))