import numpy as np 

def function(x):

	h4 = x
	r8 = x
	paths = []
	try:
		if r8 >= 0:
			h4 = h4*7
			paths.append(1)
		else:
			r8 = r8*7
			r8 = 2-r8
			paths.append(2)
		if h4 > 1:
			x = 2+4
			x = r8+5
			paths.append(3)
		else:
			r8 = r8*0
			r8 = 6+x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))