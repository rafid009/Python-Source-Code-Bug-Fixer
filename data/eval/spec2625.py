import numpy as np 

def function(x):

	u9 = 9
	b5 = x
	paths = []
	try:
		if u9 >= 1:
			u9 = x/u9
			paths.append(1)
		else:
			x = x-1
			u9 = u9/x
			x = 2*1
			paths.append(2)
		if b5 > 3:
			b5 = 5-u9
			u9 = u9-x
			paths.append(3)
		else:
			x = b5*u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		b5 = u9**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))