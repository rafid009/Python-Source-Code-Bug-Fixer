import numpy as np 

def function(x):

	v6 = x
	h5 = 2
	paths = []
	try:
		if h5 <= 5:
			h5 = h5-1
			paths.append(1)
		else:
			v6 = v6+7
			paths.append(2)
		if x >= 3:
			x = x+5
			x = 8*0
			paths.append(3)
		else:
			h5 = h5+7
			h5 = x+6
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		v6 = h5**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))