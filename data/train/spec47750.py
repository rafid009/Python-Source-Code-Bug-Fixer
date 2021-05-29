import numpy as np 

def function(x):

	p9 = x
	y0 = x
	paths = []
	try:
		if p9 >= 5:
			x = x-8
			x = 9/x
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if y0 <= 4:
			x = 4+p9
			paths.append(3)
		else:
			p9 = p9-p9
			p9 = 1+2
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		y0 = p9**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))