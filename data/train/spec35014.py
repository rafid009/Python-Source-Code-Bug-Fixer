import numpy as np 

def function(x):

	u9 = 8
	d2 = 3
	paths = []
	try:
		if u9 < 3:
			u9 = u9*u9
			d2 = d2*1
			paths.append(1)
		else:
			u9 = d2*1
			d2 = 6+d2
			u9 = u9+6
			paths.append(2)
		if d2 > 2:
			u9 = 5*3
			u9 = d2*9
			u9 = d2+x
			paths.append(3)
		else:
			u9 = u9-5
			x = 5+6
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))