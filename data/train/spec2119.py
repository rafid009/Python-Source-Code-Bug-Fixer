import numpy as np 

def function(x):

	e8 = x
	u6 = 7
	paths = []
	try:
		if u6 <= 6:
			u6 = x-u6
			e8 = e8+3
			paths.append(1)
		else:
			x = 7/9
			u6 = u6*4
			paths.append(2)
		if u6 <= 1:
			u6 = x*4
			paths.append(3)
		else:
			u6 = u6+1
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))