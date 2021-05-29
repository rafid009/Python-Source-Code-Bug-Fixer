import numpy as np 

def function(x):

	h7 = x
	f5 = x
	paths = []
	try:
		if h7 < 2:
			f5 = f5*7
			f5 = f5*2
			paths.append(1)
		else:
			h7 = h7/h7
			paths.append(2)
		if f5 >= 7:
			h7 = h7/4
			x = x*0
			f5 = 7-x
			paths.append(3)
		else:
			x = 9*4
			x = x/1
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		h7 = f5**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))