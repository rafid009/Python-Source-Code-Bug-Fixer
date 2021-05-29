import numpy as np 

def function(x):

	o2 = x
	u5 = x
	paths = []
	try:
		if x < 7:
			x = u5*x
			u5 = 6/7
			paths.append(1)
		else:
			x = 3-o2
			paths.append(2)
		if o2 < 4:
			u5 = u5*6
			o2 = o2-x
			u5 = 9-u5
			paths.append(3)
		else:
			x = x*o2
			o2 = o2+5
			u5 = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))