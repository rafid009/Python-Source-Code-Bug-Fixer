import numpy as np 

def function(x):

	f9 = x
	u5 = 4
	x = 6
	paths = []
	try:
		if u5 < 2:
			u5 = f9/3
			x = u5+8
			paths.append(1)
		else:
			f9 = f9-f9
			f9 = f9/2
			paths.append(2)
		if x >= 5:
			u5 = 5*2
			u5 = 2+0
			u5 = f9-4
			paths.append(3)
		else:
			u5 = x/4
			f9 = f9*8
			f9 = 9-f9
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))