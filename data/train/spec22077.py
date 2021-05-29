import numpy as np 

def function(x):

	u7 = 5
	b5 = x
	paths = []
	try:
		if x <= 6:
			b5 = b5+9
			x = x+6
			paths.append(1)
		else:
			x = u7-3
			u7 = 2-u7
			paths.append(2)
		if u7 <= 0:
			u7 = u7+5
			x = 1/x
			u7 = u7/2
			paths.append(3)
		else:
			u7 = b5*8
			u7 = 5+b5
			b5 = x-b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		u7 = b5**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))