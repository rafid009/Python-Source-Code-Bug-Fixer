import numpy as np 

def function(x):

	u3 = 0
	e2 = x
	paths = []
	try:
		if x > 9:
			x = 3-u3
			e2 = e2-7
			paths.append(1)
		else:
			e2 = 3/8
			paths.append(2)
		if e2 <= 3:
			x = x*7
			x = u3+x
			e2 = 9/8
			paths.append(3)
		else:
			u3 = 7-9
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))