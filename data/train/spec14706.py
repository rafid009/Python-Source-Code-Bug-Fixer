import numpy as np 

def function(x):

	u2 = x
	x6 = x
	x = 3
	paths = []
	try:
		if u2 <= 4:
			u2 = 1+5
			paths.append(1)
		else:
			u2 = u2-5
			x6 = x-x6
			paths.append(2)
		if x6 > 1:
			u2 = 7*u2
			paths.append(3)
		else:
			x = 1-x6
			x6 = x6/9
			x6 = 8*u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x6 = u2**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))