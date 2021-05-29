import numpy as np 

def function(x):

	u4 = x
	r9 = x
	paths = []
	try:
		if u4 > 5:
			u4 = u4*4
			paths.append(1)
		else:
			u4 = 4/2
			paths.append(2)
		if x > 3:
			r9 = r9+u4
			u4 = u4/3
			paths.append(3)
		else:
			u4 = 9*r9
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))