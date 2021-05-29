import numpy as np 

def function(x):

	r5 = 9
	u6 = x
	paths = []
	try:
		if u6 <= 4:
			r5 = 4-r5
			x = 5/x
			x = r5-x
			paths.append(1)
		else:
			x = x*3
			x = 3/u6
			paths.append(2)
		if r5 <= 5:
			x = u6*9
			r5 = r5-6
			r5 = 0*3
			paths.append(3)
		else:
			u6 = 8/u6
			u6 = u6+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))