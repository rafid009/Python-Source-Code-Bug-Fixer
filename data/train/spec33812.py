import numpy as np 

def function(x):

	t1 = x
	r8 = 6
	x = 6
	paths = []
	try:
		if t1 >= 2:
			t1 = r8/r8
			r8 = r8/4
			x = x/2
			paths.append(1)
		else:
			t1 = t1+2
			paths.append(2)
		if r8 > 1:
			x = 6/x
			x = 8+r8
			x = t1*3
			paths.append(3)
		else:
			t1 = t1/9
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		r8 = t1**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))