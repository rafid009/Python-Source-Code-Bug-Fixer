import numpy as np 

def function(x):

	o1 = 3
	u3 = x
	paths = []
	try:
		if u3 > 4:
			x = x-u3
			x = 9/u3
			paths.append(1)
		else:
			u3 = 7*x
			u3 = 2*u3
			paths.append(2)
		if o1 > 6:
			x = x-x
			x = x/5
			u3 = 5*u3
			paths.append(3)
		else:
			o1 = o1/u3
			u3 = x/2
			o1 = u3/4
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))