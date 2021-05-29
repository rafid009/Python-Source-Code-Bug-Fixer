import numpy as np 

def function(x):

	u3 = x
	d4 = x
	paths = []
	try:
		if d4 < 7:
			d4 = d4*3
			d4 = d4*d4
			paths.append(1)
		else:
			d4 = d4-0
			u3 = u3*0
			paths.append(2)
		if d4 < 9:
			u3 = u3/6
			paths.append(3)
		else:
			x = 6*d4
			u3 = u3/6
			u3 = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))