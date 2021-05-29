import numpy as np 

def function(x):

	r9 = 5
	u5 = 6
	paths = []
	try:
		if u5 >= 4:
			u5 = 3*u5
			u5 = u5/1
			paths.append(1)
		else:
			x = 2*4
			paths.append(2)
		if x > 6:
			u5 = 9-u5
			x = r9-7
			paths.append(3)
		else:
			r9 = r9/7
			x = x+4
			r9 = r9-2
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		u5 = r9**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))