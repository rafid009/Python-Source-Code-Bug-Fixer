import numpy as np 

def function(x):

	i3 = x
	u5 = 3
	paths = []
	try:
		if i3 >= 3:
			u5 = u5+1
			paths.append(1)
		else:
			x = 6+i3
			paths.append(2)
		if i3 > 8:
			u5 = 2*u5
			u5 = 2-7
			paths.append(3)
		else:
			u5 = u5+5
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