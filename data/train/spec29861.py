import numpy as np 

def function(x):

	o4 = x
	u3 = 2
	x = x
	paths = []
	try:
		if x > 5:
			u3 = 6-1
			o4 = o4/5
			paths.append(1)
		else:
			x = 9/u3
			paths.append(2)
		if x <= 8:
			x = x*5
			x = 2-x
			paths.append(3)
		else:
			x = u3-0
			o4 = o4-4
			u3 = u3/6
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))