import numpy as np 

def function(x):

	t7 = 6
	r2 = x
	x = 7
	paths = []
	try:
		if r2 >= 4:
			t7 = 4*0
			r2 = x-r2
			paths.append(1)
		else:
			t7 = 4-t7
			t7 = 9+t7
			r2 = 3-r2
			paths.append(2)
		if r2 >= 0:
			x = x-9
			t7 = t7/8
			paths.append(3)
		else:
			t7 = t7*8
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))