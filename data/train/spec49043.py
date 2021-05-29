import numpy as np 

def function(x):

	t4 = 4
	v3 = x
	paths = []
	try:
		if v3 <= 5:
			t4 = t4*1
			x = x-5
			x = x-t4
			paths.append(1)
		else:
			x = t4/x
			v3 = v3+v3
			paths.append(2)
		if v3 >= 5:
			x = 2+v3
			x = x+t4
			paths.append(3)
		else:
			v3 = v3-x
			x = x*t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))