import numpy as np 

def function(x):

	t1 = 3
	r8 = x
	paths = []
	try:
		if r8 <= 4:
			r8 = r8-2
			paths.append(1)
		else:
			x = x*r8
			paths.append(2)
		if x > 9:
			t1 = r8+t1
			paths.append(3)
		else:
			r8 = 4/t1
			r8 = r8+0
			r8 = r8-t1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))