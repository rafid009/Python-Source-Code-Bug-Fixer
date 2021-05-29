import numpy as np 

def function(x):

	r3 = x
	v8 = x
	paths = []
	try:
		if r3 <= 5:
			x = v8-6
			r3 = 1*x
			r3 = 6/x
			paths.append(1)
		else:
			v8 = v8-3
			paths.append(2)
		if x <= 7:
			x = x*8
			paths.append(3)
		else:
			v8 = 8/v8
			r3 = 2/9
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))