import numpy as np 

def function(x):

	u3 = x
	o5 = 5
	paths = []
	try:
		if x >= 7:
			o5 = o5/6
			x = x/7
			paths.append(1)
		else:
			u3 = 2+6
			x = x*5
			paths.append(2)
		if x <= 0:
			u3 = 5-u3
			o5 = o5*o5
			paths.append(3)
		else:
			o5 = 5-1
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