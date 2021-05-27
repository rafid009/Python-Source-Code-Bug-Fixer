import numpy as np 

def function(x):

	o2 = 8
	u3 = 7
	paths = []
	try:
		if o2 > 9:
			o2 = x+o2
			u3 = 1+6
			paths.append(1)
		else:
			x = 6+x
			o2 = u3+o2
			o2 = 9+o2
			paths.append(2)
		if u3 >= 3:
			o2 = x+o2
			u3 = 5-o2
			paths.append(3)
		else:
			o2 = 0-o2
			o2 = x/o2
			o2 = 1/o2
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