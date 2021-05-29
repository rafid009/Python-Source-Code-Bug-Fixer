import numpy as np 

def function(x):

	u2 = 2
	u3 = 0
	paths = []
	try:
		if u3 <= 2:
			x = 0+2
			u2 = u2-9
			paths.append(1)
		else:
			u2 = 4-u2
			u2 = u3/7
			u2 = u2*u3
			paths.append(2)
		if u3 <= 1:
			x = u2+x
			x = 2/u2
			u3 = 3+0
			paths.append(3)
		else:
			u2 = u2*0
			u2 = u3-x
			u2 = u2+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))