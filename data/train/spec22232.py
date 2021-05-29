import numpy as np 

def function(x):

	r3 = 7
	t6 = x
	paths = []
	try:
		if x > 3:
			x = 6*3
			t6 = t6-r3
			r3 = t6/r3
			paths.append(1)
		else:
			x = x*1
			t6 = t6/7
			x = x-9
			paths.append(2)
		if x < 8:
			r3 = t6-5
			paths.append(3)
		else:
			x = x*x
			r3 = t6*r3
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