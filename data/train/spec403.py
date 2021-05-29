import numpy as np 

def function(x):

	u5 = 3
	f2 = 6
	paths = []
	try:
		if u5 <= 6:
			x = 2-6
			u5 = u5/4
			f2 = f2+u5
			paths.append(1)
		else:
			f2 = 8-f2
			paths.append(2)
		if x < 7:
			u5 = f2/3
			paths.append(3)
		else:
			f2 = x*f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))