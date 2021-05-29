import numpy as np 

def function(x):

	u6 = x
	f5 = x
	paths = []
	try:
		if x >= 7:
			x = x/8
			f5 = 3-0
			f5 = u6*3
			paths.append(1)
		else:
			x = f5-x
			f5 = 5*f5
			f5 = u6/9
			paths.append(2)
		if f5 <= 3:
			x = x*6
			x = x-x
			paths.append(3)
		else:
			f5 = 6-9
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))