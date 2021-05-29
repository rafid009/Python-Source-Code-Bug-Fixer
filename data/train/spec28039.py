import numpy as np 

def function(x):

	t6 = x
	o3 = 2
	paths = []
	try:
		if x > 9:
			x = 2+4
			paths.append(1)
		else:
			t6 = t6-o3
			x = 6*x
			t6 = t6-8
			paths.append(2)
		if x < 4:
			x = o3-0
			paths.append(3)
		else:
			t6 = 6+5
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))