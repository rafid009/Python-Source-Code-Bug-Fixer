import numpy as np 

def function(x):

	b2 = 2
	u9 = 6
	paths = []
	try:
		if u9 <= 0:
			x = x/x
			u9 = u9*6
			x = 7+u9
			paths.append(1)
		else:
			u9 = 3*3
			u9 = u9*5
			b2 = 7+4
			paths.append(2)
		if u9 <= 6:
			u9 = u9-6
			u9 = x+x
			u9 = x/u9
			paths.append(3)
		else:
			b2 = u9/u9
			b2 = b2+x
			u9 = b2/u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))