import numpy as np 

def function(x):

	y4 = x
	f8 = x
	paths = []
	try:
		if x <= 3:
			x = 1+f8
			paths.append(1)
		else:
			f8 = f8*0
			x = 2+x
			x = 5-2
			paths.append(2)
		if x >= 6:
			x = x*y4
			paths.append(3)
		else:
			f8 = f8*8
			y4 = y4*4
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		y4 = f8**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))