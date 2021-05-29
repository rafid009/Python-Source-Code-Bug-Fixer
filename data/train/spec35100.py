import numpy as np 

def function(x):

	o2 = x
	h8 = x
	paths = []
	try:
		if h8 > 1:
			x = x*6
			paths.append(1)
		else:
			h8 = 1-h8
			o2 = o2+0
			x = o2/2
			paths.append(2)
		if o2 >= 6:
			o2 = 6*h8
			x = x+7
			paths.append(3)
		else:
			h8 = h8-2
			h8 = h8*0
			h8 = 8+x
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))