import numpy as np 

def function(x):

	o1 = x
	u9 = x
	x = 8
	paths = []
	try:
		if u9 < 9:
			u9 = u9/3
			u9 = 0+o1
			paths.append(1)
		else:
			o1 = o1+2
			x = 0-x
			paths.append(2)
		if o1 >= 9:
			o1 = u9-o1
			u9 = 7*2
			paths.append(3)
		else:
			u9 = o1*u9
			u9 = u9-u9
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		u9 = o1**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))