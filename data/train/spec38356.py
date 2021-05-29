import numpy as np 

def function(x):

	t8 = x
	r6 = x
	paths = []
	try:
		if x <= 0:
			r6 = r6/6
			x = t8+1
			paths.append(1)
		else:
			x = r6/x
			r6 = 8*2
			paths.append(2)
		if t8 <= 2:
			t8 = 6/1
			r6 = 4/x
			paths.append(3)
		else:
			r6 = r6+4
			x = r6+3
			x = t8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))