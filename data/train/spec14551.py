import numpy as np 

def function(x):

	u7 = x
	f5 = x
	paths = []
	try:
		if x < 2:
			x = x+u7
			paths.append(1)
		else:
			f5 = 4/f5
			paths.append(2)
		if f5 >= 3:
			x = 0/6
			f5 = f5+1
			paths.append(3)
		else:
			f5 = x+2
			f5 = 1-3
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))