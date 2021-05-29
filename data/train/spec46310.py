import numpy as np 

def function(x):

	r9 = 8
	f5 = x
	paths = []
	try:
		if x > 3:
			x = x/1
			f5 = 7+f5
			paths.append(1)
		else:
			r9 = 8-r9
			r9 = r9*9
			paths.append(2)
		if x < 5:
			x = x-1
			f5 = x-2
			f5 = 2-6
			paths.append(3)
		else:
			x = 1-x
			x = x/4
			f5 = f5+f5
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