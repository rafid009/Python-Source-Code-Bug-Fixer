import numpy as np 

def function(x):

	o9 = 5
	u7 = 8
	paths = []
	try:
		if x > 5:
			u7 = 6*0
			o9 = o9/o9
			x = x/x
			paths.append(1)
		else:
			o9 = 2*8
			paths.append(2)
		if u7 > 4:
			u7 = x/u7
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))