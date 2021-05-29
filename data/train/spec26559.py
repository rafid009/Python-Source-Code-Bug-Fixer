import numpy as np 

def function(x):

	e3 = x
	u1 = x
	paths = []
	try:
		if x >= 1:
			x = x+6
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if u1 > 3:
			x = x/3
			u1 = u1*x
			e3 = u1*2
			paths.append(3)
		else:
			u1 = x*2
			x = 9*x
			x = x+7
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))