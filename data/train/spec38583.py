import numpy as np 

def function(x):

	f8 = x
	w4 = x
	x = x
	paths = []
	try:
		if x < 4:
			x = 6-x
			x = 2/f8
			w4 = w4/7
			paths.append(1)
		else:
			x = x-7
			w4 = f8-5
			paths.append(2)
		if x <= 6:
			w4 = w4-x
			paths.append(3)
		else:
			x = 1*x
			x = x/5
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))