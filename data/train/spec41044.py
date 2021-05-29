import numpy as np 

def function(x):

	t4 = x
	r5 = 4
	x = x
	paths = []
	try:
		if r5 >= 9:
			t4 = 8/t4
			x = x/8
			r5 = r5-8
			paths.append(1)
		else:
			x = t4+x
			x = x-5
			r5 = 8+r5
			paths.append(2)
		if r5 >= 4:
			t4 = t4-7
			x = x+r5
			t4 = x+t4
			paths.append(3)
		else:
			x = x*t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))