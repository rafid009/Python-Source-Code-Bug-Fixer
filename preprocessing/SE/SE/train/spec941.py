import numpy as np 

def function(x):

	r8 = 6
	h8 = 9
	paths = []
	try:
		if x > 4:
			x = x/7
			x = x+x
			paths.append(1)
		else:
			h8 = 8/h8
			r8 = r8/x
			h8 = h8*r8
			paths.append(2)
		if r8 <= 2:
			x = x+x
			r8 = r8*4
			r8 = r8-0
			paths.append(3)
		else:
			r8 = r8-0
			r8 = 5-9
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		h8 = r8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))