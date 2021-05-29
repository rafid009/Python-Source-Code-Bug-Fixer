import numpy as np 

def function(x):

	p8 = 3
	f8 = 3
	paths = []
	try:
		if f8 > 3:
			f8 = f8/6
			paths.append(1)
		else:
			p8 = p8/f8
			paths.append(2)
		if x > 3:
			p8 = f8/p8
			f8 = 6+f8
			p8 = x*p8
			paths.append(3)
		else:
			x = p8+x
			p8 = f8-p8
			p8 = p8-x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))