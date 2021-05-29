import numpy as np 

def function(x):

	u9 = x
	u6 = x
	x = 0
	paths = []
	try:
		if u6 >= 4:
			x = x+1
			x = 5-x
			x = x+7
			paths.append(1)
		else:
			x = 7+x
			u6 = u6-u6
			u6 = u6*4
			paths.append(2)
		if u6 < 4:
			x = x+5
			u9 = 0-x
			paths.append(3)
		else:
			u9 = u9-3
			x = x*8
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))