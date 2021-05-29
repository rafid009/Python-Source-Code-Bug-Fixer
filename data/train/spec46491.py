import numpy as np 

def function(x):

	r8 = x
	t6 = 2
	paths = []
	try:
		if t6 < 2:
			r8 = 3+r8
			t6 = t6*x
			r8 = 2-x
			paths.append(1)
		else:
			r8 = 0-r8
			paths.append(2)
		if x < 4:
			t6 = t6/1
			t6 = 8/5
			x = 4+x
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))