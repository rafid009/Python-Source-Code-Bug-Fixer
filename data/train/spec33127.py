import numpy as np 

def function(x):

	h6 = x
	v6 = x
	paths = []
	try:
		if h6 >= 9:
			h6 = h6+0
			paths.append(1)
		else:
			v6 = 1-v6
			v6 = 2*2
			v6 = v6-8
			paths.append(2)
		if v6 <= 7:
			h6 = v6-0
			paths.append(3)
		else:
			v6 = 7*v6
			x = x/5
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))