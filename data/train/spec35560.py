import numpy as np 

def function(x):

	h4 = x
	i9 = x
	paths = []
	try:
		if x > 7:
			h4 = 2/h4
			i9 = x+0
			h4 = h4/h4
			paths.append(1)
		else:
			x = x*8
			x = x+1
			x = i9/2
			paths.append(2)
		if h4 <= 2:
			h4 = h4*6
			i9 = h4-i9
			paths.append(3)
		else:
			h4 = h4-i9
			x = x*0
			h4 = 2*h4
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		h4 = i9**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))