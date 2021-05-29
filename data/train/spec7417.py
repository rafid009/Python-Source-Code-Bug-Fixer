import numpy as np 

def function(x):

	f6 = x
	x1 = 5
	paths = []
	try:
		if x1 >= 4:
			x = x/7
			x1 = x1*0
			x = 2*6
			paths.append(1)
		else:
			x1 = 2/x1
			x = x-0
			paths.append(2)
		if x1 >= 4:
			x1 = 3+7
			paths.append(3)
		else:
			x1 = 9*f6
			f6 = 6*9
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		f6 = x1**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))