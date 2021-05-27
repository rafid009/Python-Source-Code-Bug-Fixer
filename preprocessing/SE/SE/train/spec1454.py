import numpy as np 

def function(x):

	o0 = 8
	r6 = x
	paths = []
	try:
		if r6 < 9:
			r6 = x+7
			o0 = o0*x
			paths.append(1)
		else:
			x = 4/3
			paths.append(2)
		if r6 > 2:
			x = x/4
			x = 9*x
			paths.append(3)
		else:
			r6 = 8*x
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		o0 = r6**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))