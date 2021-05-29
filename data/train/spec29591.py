import numpy as np 

def function(x):

	e0 = 1
	u3 = x
	paths = []
	try:
		if u3 < 7:
			x = 1+e0
			e0 = e0/u3
			u3 = e0+u3
			paths.append(1)
		else:
			x = x-1
			u3 = u3+1
			x = x+9
			paths.append(2)
		if u3 > 0:
			u3 = 6*u3
			x = x*4
			paths.append(3)
		else:
			e0 = e0+5
			x = x+u3
			u3 = u3/1
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