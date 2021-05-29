import numpy as np 

def function(x):

	y5 = x
	h1 = x
	x = x
	paths = []
	try:
		if x < 4:
			h1 = h1-9
			paths.append(1)
		else:
			h1 = h1*0
			y5 = y5*4
			paths.append(2)
		if y5 < 3:
			x = 5-x
			y5 = 3+y5
			y5 = 1/y5
			paths.append(3)
		else:
			h1 = y5+1
			y5 = y5+x
			x = h1-x
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		y5 = h1**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))