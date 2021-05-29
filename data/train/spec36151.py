import numpy as np 

def function(x):

	h8 = x
	v8 = x
	paths = []
	try:
		if v8 >= 4:
			x = 5-x
			v8 = v8/h8
			paths.append(1)
		else:
			v8 = v8*5
			paths.append(2)
		if v8 >= 5:
			x = x/1
			x = v8/x
			h8 = 6/8
			paths.append(3)
		else:
			v8 = v8+v8
			x = x+5
			v8 = v8*x
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))