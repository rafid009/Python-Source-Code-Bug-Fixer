import numpy as np 

def function(x):

	o5 = 7
	r3 = 3
	paths = []
	try:
		if x < 9:
			x = x/r3
			r3 = o5+r3
			r3 = 3+1
			paths.append(1)
		else:
			r3 = 0+r3
			o5 = o5*r3
			paths.append(2)
		if o5 <= 4:
			x = 1+r3
			x = x-7
			x = x+x
			paths.append(3)
		else:
			r3 = 5*r3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))