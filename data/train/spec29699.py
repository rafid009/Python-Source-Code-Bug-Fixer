import numpy as np 

def function(x):

	t9 = 0
	r7 = 2
	paths = []
	try:
		if r7 <= 4:
			r7 = r7/5
			x = x-r7
			paths.append(1)
		else:
			x = x*x
			r7 = 9-9
			paths.append(2)
		if t9 > 0:
			r7 = 5+r7
			r7 = r7+x
			t9 = 8/t9
			paths.append(3)
		else:
			t9 = 8+t9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))