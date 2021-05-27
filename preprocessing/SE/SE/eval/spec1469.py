import numpy as np 

def function(x):

	h2 = x
	u5 = x
	paths = []
	try:
		if x <= 5:
			x = x*3
			paths.append(1)
		else:
			h2 = 3*h2
			h2 = h2-x
			u5 = u5/9
			paths.append(2)
		if u5 >= 4:
			x = x-x
			x = x+u5
			paths.append(3)
		else:
			u5 = 3/h2
			u5 = 4-u5
			h2 = 6/h2
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		h2 = u5**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))