import numpy as np 

def function(x):

	p8 = x
	j8 = x
	paths = []
	try:
		if x <= 3:
			j8 = 2-j8
			paths.append(1)
		else:
			x = 3-j8
			j8 = x*3
			paths.append(2)
		if p8 > 2:
			p8 = p8/j8
			p8 = 0-p8
			j8 = x/7
			paths.append(3)
		else:
			j8 = j8-3
			x = 1/x
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