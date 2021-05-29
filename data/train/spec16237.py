import numpy as np 

def function(x):

	u3 = x
	y4 = 6
	paths = []
	try:
		if u3 > 7:
			u3 = y4*3
			y4 = y4/u3
			paths.append(1)
		else:
			y4 = y4/u3
			y4 = y4+8
			paths.append(2)
		if x > 7:
			y4 = y4/3
			u3 = 6-y4
			u3 = u3-4
			paths.append(3)
		else:
			u3 = 7+u3
			y4 = y4/9
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		u3 = y4**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))