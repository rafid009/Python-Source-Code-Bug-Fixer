import numpy as np 

def function(x):

	d8 = 2
	u9 = 8
	paths = []
	try:
		if u9 <= 7:
			u9 = u9+x
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if d8 < 0:
			u9 = u9+2
			x = d8+d8
			paths.append(3)
		else:
			u9 = 1-4
			u9 = 8-x
			x = 6+4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		d8 = u9**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))