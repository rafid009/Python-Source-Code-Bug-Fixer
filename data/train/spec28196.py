import numpy as np 

def function(x):

	u3 = x
	o6 = 3
	paths = []
	try:
		if o6 < 5:
			u3 = u3+3
			x = x*8
			o6 = o6-9
			paths.append(1)
		else:
			x = 1-u3
			x = x*3
			u3 = 2+8
			paths.append(2)
		if u3 >= 8:
			u3 = 6-o6
			x = u3/o6
			paths.append(3)
		else:
			x = x/o6
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