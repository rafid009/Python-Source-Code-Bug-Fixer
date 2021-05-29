import numpy as np 

def function(x):

	r9 = x
	y4 = x
	paths = []
	try:
		if y4 < 5:
			x = x/7
			r9 = 2+r9
			paths.append(1)
		else:
			y4 = 3+4
			x = x*1
			r9 = x+x
			paths.append(2)
		if x <= 8:
			x = x+0
			paths.append(3)
		else:
			x = x+4
			x = 5+x
			r9 = 3-r9
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))