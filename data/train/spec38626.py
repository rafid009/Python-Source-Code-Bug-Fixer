import numpy as np 

def function(x):

	l2 = x
	u5 = 8
	x = x
	paths = []
	try:
		if x > 8:
			x = x/1
			u5 = 3/u5
			l2 = 7+l2
			paths.append(1)
		else:
			u5 = u5/u5
			paths.append(2)
		if l2 < 3:
			u5 = x+u5
			u5 = l2+u5
			u5 = u5+l2
			paths.append(3)
		else:
			x = x+4
			l2 = l2*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))