import numpy as np 

def function(x):

	h2 = x
	f3 = x
	paths = []
	try:
		if h2 <= 6:
			h2 = h2*9
			paths.append(1)
		else:
			x = x*3
			h2 = 8/h2
			paths.append(2)
		if h2 < 7:
			x = x/8
			x = 8+3
			f3 = x*h2
			paths.append(3)
		else:
			h2 = h2*1
			x = 9/9
			f3 = 6/f3
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		f3 = h2**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))