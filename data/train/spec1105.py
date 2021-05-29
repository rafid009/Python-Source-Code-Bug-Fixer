import numpy as np 

def function(x):

	o1 = x
	r6 = 4
	paths = []
	try:
		if r6 <= 8:
			o1 = 6*x
			x = x+x
			paths.append(1)
		else:
			o1 = r6*x
			r6 = r6*7
			r6 = 3/7
			paths.append(2)
		if x <= 0:
			r6 = r6-5
			x = 0-r6
			o1 = o1/3
			paths.append(3)
		else:
			o1 = x+o1
			x = x/r6
			o1 = 0+5
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		r6 = o1**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))