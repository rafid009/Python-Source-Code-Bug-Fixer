import numpy as np 

def function(x):

	o1 = x
	u9 = x
	paths = []
	try:
		if u9 > 0:
			x = 8*x
			u9 = u9+9
			paths.append(1)
		else:
			x = x-4
			o1 = 6+9
			o1 = o1+2
			paths.append(2)
		if x < 6:
			x = x/o1
			paths.append(3)
		else:
			o1 = x/5
			u9 = u9/6
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		o1 = u9**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))