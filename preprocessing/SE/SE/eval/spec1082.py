import numpy as np 

def function(x):

	f8 = x
	h9 = 0
	x = 7
	paths = []
	try:
		if f8 < 5:
			h9 = h9-h9
			f8 = 7*8
			paths.append(1)
		else:
			f8 = f8-8
			h9 = f8*9
			x = 1-x
			paths.append(2)
		if x <= 8:
			x = x+1
			f8 = f8+x
			paths.append(3)
		else:
			x = x*h9
			f8 = f8+7
			f8 = f8-1
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