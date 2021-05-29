import numpy as np 

def function(x):

	k6 = 3
	u0 = 2
	paths = []
	try:
		if u0 < 4:
			u0 = k6+u0
			paths.append(1)
		else:
			u0 = u0/u0
			u0 = x*k6
			paths.append(2)
		if u0 <= 9:
			u0 = u0-9
			x = x/4
			paths.append(3)
		else:
			u0 = 4/9
			x = x/8
			k6 = k6-9
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		k6 = u0**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))