import numpy as np 

def function(x):

	i5 = 8
	u1 = x
	paths = []
	try:
		if u1 > 2:
			u1 = u1-x
			paths.append(1)
		else:
			u1 = x*u1
			x = x+3
			paths.append(2)
		if i5 > 1:
			i5 = i5+x
			u1 = i5*i5
			paths.append(3)
		else:
			u1 = 9*x
			x = u1+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))