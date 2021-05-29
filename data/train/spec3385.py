import numpy as np 

def function(x):

	h7 = x
	f8 = 7
	paths = []
	try:
		if h7 <= 6:
			f8 = f8*3
			f8 = f8+f8
			paths.append(1)
		else:
			h7 = h7+3
			h7 = 7+h7
			paths.append(2)
		if f8 <= 7:
			f8 = f8-f8
			x = x+7
			h7 = h7-0
			paths.append(3)
		else:
			f8 = f8/x
			f8 = f8/9
			x = x+6
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))