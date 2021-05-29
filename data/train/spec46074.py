import numpy as np 

def function(x):

	o6 = x
	u3 = x
	paths = []
	try:
		if u3 >= 3:
			u3 = u3/o6
			o6 = o6/o6
			paths.append(1)
		else:
			x = u3+o6
			u3 = 5/u3
			o6 = u3*2
			paths.append(2)
		if x <= 4:
			u3 = o6-8
			u3 = u3*o6
			x = 6+u3
			paths.append(3)
		else:
			u3 = 1*u3
			u3 = u3*o6
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))