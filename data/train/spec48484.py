import numpy as np 

def function(x):

	y1 = 2
	u3 = 6
	paths = []
	try:
		if y1 <= 4:
			y1 = y1*2
			paths.append(1)
		else:
			y1 = y1-7
			y1 = y1+u3
			u3 = 9-u3
			paths.append(2)
		if y1 > 5:
			x = 5+y1
			u3 = u3+4
			x = 7/x
			paths.append(3)
		else:
			y1 = u3-x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		u3 = y1**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))