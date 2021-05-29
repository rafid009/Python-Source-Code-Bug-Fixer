import numpy as np 

def function(x):

	u5 = 5
	f2 = x
	paths = []
	try:
		if x >= 1:
			x = 8+x
			paths.append(1)
		else:
			f2 = 7/f2
			x = 3-x
			f2 = f2+f2
			paths.append(2)
		if f2 < 7:
			u5 = 7/u5
			paths.append(3)
		else:
			u5 = u5-0
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		u5 = f2**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))