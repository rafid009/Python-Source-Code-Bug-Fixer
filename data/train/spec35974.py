import numpy as np 

def function(x):

	u7 = 3
	y2 = x
	paths = []
	try:
		if y2 > 9:
			x = y2+6
			y2 = 8+u7
			y2 = u7-3
			paths.append(1)
		else:
			x = y2/x
			paths.append(2)
		if u7 <= 3:
			x = x+0
			y2 = y2+1
			paths.append(3)
		else:
			u7 = 2*u7
			x = x*8
			y2 = y2*7
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		u7 = y2**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))