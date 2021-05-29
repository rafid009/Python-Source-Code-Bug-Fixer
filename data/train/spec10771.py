import numpy as np 

def function(x):

	t4 = 6
	v6 = 9
	paths = []
	try:
		if x > 0:
			t4 = 5+t4
			paths.append(1)
		else:
			x = x*v6
			x = 7/x
			v6 = v6/3
			paths.append(2)
		if v6 >= 1:
			t4 = t4*x
			x = x/x
			t4 = 8-t4
			paths.append(3)
		else:
			t4 = 4/4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		v6 = t4**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))