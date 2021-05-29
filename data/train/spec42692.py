import numpy as np 

def function(x):

	v6 = x
	h3 = 1
	paths = []
	try:
		if x <= 3:
			x = x-x
			x = x/5
			paths.append(1)
		else:
			x = x+x
			v6 = x-x
			x = x+9
			paths.append(2)
		if h3 <= 5:
			v6 = v6-6
			h3 = h3+6
			h3 = x/7
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		h3 = v6**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))