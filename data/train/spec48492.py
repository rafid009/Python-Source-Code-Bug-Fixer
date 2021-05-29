import numpy as np 

def function(x):

	u5 = x
	f7 = x
	paths = []
	try:
		if f7 <= 8:
			f7 = f7/2
			f7 = 3+u5
			paths.append(1)
		else:
			f7 = 6+x
			paths.append(2)
		if f7 >= 8:
			x = x/6
			f7 = 1/f7
			u5 = 6+u5
			paths.append(3)
		else:
			f7 = 2+f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		u5 = f7**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))