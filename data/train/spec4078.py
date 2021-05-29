import numpy as np 

def function(x):

	a1 = 8
	u4 = x
	paths = []
	try:
		if x <= 2:
			u4 = 0+u4
			a1 = 2-a1
			paths.append(1)
		else:
			x = x-2
			x = 0+6
			paths.append(2)
		if u4 > 5:
			a1 = 0-a1
			x = x*a1
			u4 = u4/6
			paths.append(3)
		else:
			x = x+1
			u4 = 4/u4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		a1 = u4**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))