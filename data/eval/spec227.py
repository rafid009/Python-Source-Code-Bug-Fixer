import numpy as np 

def function(x):

	r6 = 8
	t1 = x
	paths = []
	try:
		if r6 > 5:
			t1 = r6-x
			paths.append(1)
		else:
			x = x/8
			x = 6/x
			r6 = 0+r6
			paths.append(2)
		if r6 >= 0:
			t1 = x*9
			paths.append(3)
		else:
			x = 3+6
			r6 = 5*9
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		r6 = t1**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))