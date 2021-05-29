import numpy as np 

def function(x):

	b0 = x
	u5 = 1
	paths = []
	try:
		if b0 > 7:
			x = x/6
			x = x*6
			paths.append(1)
		else:
			b0 = 0-4
			u5 = 2-x
			paths.append(2)
		if x <= 0:
			b0 = b0+9
			x = 0-x
			paths.append(3)
		else:
			b0 = 0+b0
			u5 = 4-5
			u5 = u5*8
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		b0 = u5**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))