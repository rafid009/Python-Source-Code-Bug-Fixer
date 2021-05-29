import numpy as np 

def function(x):

	w5 = x
	r5 = x
	paths = []
	try:
		if r5 <= 6:
			r5 = r5+x
			x = 0+4
			paths.append(1)
		else:
			r5 = r5*9
			paths.append(2)
		if x < 2:
			x = w5+x
			r5 = 7-7
			paths.append(3)
		else:
			x = x/x
			r5 = r5+3
			x = x/4
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		r5 = w5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))