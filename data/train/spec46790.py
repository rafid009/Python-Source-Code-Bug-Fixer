import numpy as np 

def function(x):

	r5 = x
	u3 = 0
	paths = []
	try:
		if x > 3:
			u3 = 0/4
			u3 = u3/6
			u3 = 9+r5
			paths.append(1)
		else:
			r5 = r5/5
			x = 4/x
			r5 = r5+3
			paths.append(2)
		if x < 1:
			u3 = 9+u3
			u3 = x-u3
			x = 4+3
			paths.append(3)
		else:
			x = 4-x
			x = x-r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))