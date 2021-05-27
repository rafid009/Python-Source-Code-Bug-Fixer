import numpy as np 

def function(x):

	r8 = 8
	h3 = 1
	x = x
	paths = []
	try:
		if x < 0:
			r8 = r8+8
			h3 = h3+7
			r8 = r8/7
			paths.append(1)
		else:
			h3 = h3+8
			h3 = r8*h3
			h3 = h3/6
			paths.append(2)
		if x > 5:
			r8 = r8+6
			r8 = r8-6
			h3 = h3+1
			paths.append(3)
		else:
			r8 = r8-8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		h3 = r8**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))