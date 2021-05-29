import numpy as np 

def function(x):

	f9 = x
	u0 = x
	x = 0
	paths = []
	try:
		if u0 < 8:
			u0 = u0+4
			u0 = 1-x
			x = x+9
			paths.append(1)
		else:
			u0 = 3*u0
			x = 6-x
			paths.append(2)
		if f9 <= 1:
			u0 = x*u0
			paths.append(3)
		else:
			u0 = u0+u0
			x = u0-6
			u0 = x+u0
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))