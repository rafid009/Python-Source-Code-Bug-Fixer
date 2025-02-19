import numpy as np 

def function(x):

	e1 = x
	u3 = x
	paths = []
	try:
		if e1 < 9:
			e1 = e1+4
			x = x-e1
			paths.append(1)
		else:
			x = 4/x
			e1 = u3+e1
			paths.append(2)
		if e1 > 4:
			u3 = 1*x
			paths.append(3)
		else:
			e1 = e1+6
			x = 7+u3
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		u3 = e1**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))