import numpy as np 

def function(x):

	x6 = 8
	f1 = 3
	paths = []
	try:
		if x6 > 5:
			x6 = 8+x6
			paths.append(1)
		else:
			x6 = 6*f1
			f1 = x6-1
			f1 = x6/6
			paths.append(2)
		if x6 <= 7:
			x = x-x
			paths.append(3)
		else:
			x = f1+x
			x = x/x6
			x6 = x6*x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		f1 = x6**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))