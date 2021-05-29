import numpy as np 

def function(x):

	u1 = 7
	v6 = 2
	paths = []
	try:
		if x >= 2:
			v6 = 8-v6
			x = 5*4
			x = x/1
			paths.append(1)
		else:
			x = 1-2
			u1 = u1-v6
			u1 = 0-u1
			paths.append(2)
		if v6 <= 8:
			v6 = 9+v6
			u1 = u1*0
			paths.append(3)
		else:
			v6 = 1-2
			x = v6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))