import numpy as np 

def function(x):

	p6 = 4
	u5 = x
	paths = []
	try:
		if x < 7:
			p6 = 3*x
			paths.append(1)
		else:
			p6 = 6+p6
			paths.append(2)
		if x > 2:
			x = p6*x
			paths.append(3)
		else:
			x = x*8
			u5 = x+u5
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		u5 = p6**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))