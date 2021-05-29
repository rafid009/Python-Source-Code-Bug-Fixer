import numpy as np 

def function(x):

	o6 = 4
	u3 = x
	paths = []
	try:
		if x < 1:
			x = x/1
			x = x*9
			paths.append(1)
		else:
			o6 = 0-6
			paths.append(2)
		if u3 <= 6:
			x = x*o6
			paths.append(3)
		else:
			o6 = o6/8
			x = 0-x
			u3 = 2+u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))