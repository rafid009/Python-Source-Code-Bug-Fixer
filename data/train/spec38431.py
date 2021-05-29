import numpy as np 

def function(x):

	f4 = x
	p8 = x
	paths = []
	try:
		if x > 1:
			x = f4-2
			p8 = f4+9
			paths.append(1)
		else:
			p8 = p8*x
			paths.append(2)
		if x >= 3:
			x = 1-1
			p8 = p8-p8
			paths.append(3)
		else:
			x = 6/1
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))