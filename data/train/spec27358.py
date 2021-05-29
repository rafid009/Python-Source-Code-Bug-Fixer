import numpy as np 

def function(x):

	r8 = x
	h1 = 0
	paths = []
	try:
		if r8 <= 6:
			x = h1*6
			paths.append(1)
		else:
			r8 = 4*r8
			x = 5/1
			paths.append(2)
		if r8 > 4:
			h1 = h1/9
			x = 1*8
			paths.append(3)
		else:
			h1 = 7+h1
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		h1 = r8**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))