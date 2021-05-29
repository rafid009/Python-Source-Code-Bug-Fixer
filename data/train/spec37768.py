import numpy as np 

def function(x):

	i0 = 7
	t6 = x
	paths = []
	try:
		if i0 > 5:
			t6 = 1-1
			paths.append(1)
		else:
			t6 = 6/t6
			i0 = t6-1
			paths.append(2)
		if x > 1:
			i0 = 3*i0
			t6 = t6-x
			i0 = x+t6
			paths.append(3)
		else:
			t6 = x*i0
			t6 = 9-t6
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