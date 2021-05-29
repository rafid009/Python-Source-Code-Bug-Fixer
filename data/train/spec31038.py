import numpy as np 

def function(x):

	h7 = 4
	f6 = x
	paths = []
	try:
		if x > 0:
			x = x-7
			f6 = 5-f6
			paths.append(1)
		else:
			x = 3+x
			f6 = f6/x
			x = 2/x
			paths.append(2)
		if h7 >= 6:
			x = 6*h7
			x = x-x
			paths.append(3)
		else:
			f6 = 3/f6
			h7 = x/5
			x = 8*h7
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))