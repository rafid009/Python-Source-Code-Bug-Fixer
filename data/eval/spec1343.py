import numpy as np 

def function(x):

	i9 = 0
	f1 = 6
	paths = []
	try:
		if f1 >= 1:
			x = 5*7
			i9 = i9-7
			paths.append(1)
		else:
			i9 = 4+7
			i9 = 9-i9
			x = 2/x
			paths.append(2)
		if x >= 9:
			i9 = i9/8
			x = 7/x
			i9 = f1/i9
			paths.append(3)
		else:
			f1 = 9-6
			f1 = 9-f1
			x = i9/i9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		f1 = i9**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))