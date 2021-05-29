import numpy as np 

def function(x):

	r9 = x
	o1 = 7
	paths = []
	try:
		if r9 > 5:
			r9 = o1/2
			o1 = 4/o1
			r9 = r9+7
			paths.append(1)
		else:
			o1 = r9-2
			paths.append(2)
		if r9 <= 5:
			r9 = 3*r9
			paths.append(3)
		else:
			o1 = 2-5
			x = x/x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		o1 = r9**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))