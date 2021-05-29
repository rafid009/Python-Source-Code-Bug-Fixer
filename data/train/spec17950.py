import numpy as np 

def function(x):

	u7 = 3
	p7 = x
	paths = []
	try:
		if p7 > 7:
			x = x+0
			p7 = p7/3
			paths.append(1)
		else:
			p7 = p7*8
			u7 = u7-x
			paths.append(2)
		if p7 >= 3:
			u7 = 5-9
			x = 1*x
			u7 = x*x
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))