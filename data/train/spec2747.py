import numpy as np 

def function(x):

	r0 = 4
	t4 = 5
	paths = []
	try:
		if t4 < 1:
			r0 = r0+4
			t4 = t4/1
			paths.append(1)
		else:
			r0 = x/2
			x = x/7
			paths.append(2)
		if x < 0:
			t4 = t4*9
			t4 = t4-x
			r0 = 2+x
			paths.append(3)
		else:
			x = x/6
			t4 = t4-t4
			r0 = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))