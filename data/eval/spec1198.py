import numpy as np 

def function(x):

	f2 = x
	p8 = 5
	x = 5
	paths = []
	try:
		if x <= 1:
			x = f2/x
			paths.append(1)
		else:
			p8 = x/4
			paths.append(2)
		if x < 8:
			x = x/8
			paths.append(3)
		else:
			f2 = 0*5
			x = x/3
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		p8 = f2**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))