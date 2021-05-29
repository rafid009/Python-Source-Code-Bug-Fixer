import numpy as np 

def function(x):

	h7 = x
	p3 = x
	paths = []
	try:
		if x > 7:
			p3 = p3-5
			paths.append(1)
		else:
			p3 = 8/x
			p3 = x+h7
			x = x/5
			paths.append(2)
		if h7 < 9:
			x = p3+x
			x = x*4
			h7 = 9-4
			paths.append(3)
		else:
			x = 2/p3
			x = x/4
			p3 = 1+p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))