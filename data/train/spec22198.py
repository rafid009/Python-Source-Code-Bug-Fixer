import numpy as np 

def function(x):

	o3 = 8
	t0 = x
	paths = []
	try:
		if x > 7:
			o3 = o3/6
			o3 = 5-o3
			o3 = 1*5
			paths.append(1)
		else:
			t0 = x*2
			o3 = x+o3
			paths.append(2)
		if x <= 8:
			o3 = 5+5
			t0 = 2+t0
			t0 = 8+t0
			paths.append(3)
		else:
			t0 = 2-t0
			t0 = o3+7
			o3 = 7-t0
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		x = o3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))