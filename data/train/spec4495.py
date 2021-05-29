import numpy as np 

def function(x):

	w6 = 2
	u4 = x
	x = x
	paths = []
	try:
		if u4 < 2:
			w6 = 4/w6
			paths.append(1)
		else:
			w6 = w6*5
			paths.append(2)
		if x <= 2:
			x = x*1
			u4 = w6+x
			paths.append(3)
		else:
			u4 = u4/u4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))