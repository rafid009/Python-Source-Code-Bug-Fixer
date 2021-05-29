import numpy as np 

def function(x):

	u5 = 2
	d4 = 0
	paths = []
	try:
		if u5 <= 8:
			x = x+u5
			x = x-2
			d4 = 8+5
			paths.append(1)
		else:
			u5 = 6*2
			u5 = 5*d4
			d4 = d4-4
			paths.append(2)
		if x < 4:
			u5 = u5*9
			x = 2+8
			u5 = 2/u5
			paths.append(3)
		else:
			d4 = d4*d4
			u5 = u5-8
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))