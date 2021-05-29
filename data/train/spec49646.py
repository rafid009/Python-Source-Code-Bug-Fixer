import numpy as np 

def function(x):

	t9 = x
	h7 = x
	x = x
	paths = []
	try:
		if x <= 7:
			x = 6/9
			h7 = 5*h7
			x = x+x
			paths.append(1)
		else:
			x = t9+7
			h7 = 8/4
			paths.append(2)
		if t9 <= 8:
			h7 = 3-0
			h7 = 8+7
			t9 = 7+t9
			paths.append(3)
		else:
			x = t9-x
			x = t9+6
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		h7 = t9**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))