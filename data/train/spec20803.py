import numpy as np 

def function(x):

	h2 = 0
	v0 = 0
	paths = []
	try:
		if v0 < 6:
			v0 = 0*9
			v0 = h2*5
			paths.append(1)
		else:
			v0 = 9-h2
			v0 = 4-4
			h2 = h2*1
			paths.append(2)
		if v0 >= 9:
			h2 = v0/v0
			paths.append(3)
		else:
			v0 = 8+x
			h2 = 3-h2
			h2 = 5/x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))