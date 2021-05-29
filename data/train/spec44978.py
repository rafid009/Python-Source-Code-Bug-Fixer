import numpy as np 

def function(x):

	u5 = 2
	e2 = x
	x = x
	paths = []
	try:
		if x > 3:
			x = x*7
			paths.append(1)
		else:
			u5 = u5-u5
			u5 = e2*9
			paths.append(2)
		if e2 < 2:
			e2 = x+8
			paths.append(3)
		else:
			x = x*0
			u5 = 4-u5
			u5 = 1*x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))