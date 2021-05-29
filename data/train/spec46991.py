import numpy as np 

def function(x):

	t6 = x
	u6 = 5
	paths = []
	try:
		if x <= 5:
			u6 = u6-t6
			paths.append(1)
		else:
			u6 = 3/8
			u6 = u6*0
			t6 = t6-1
			paths.append(2)
		if x <= 5:
			x = 8-8
			t6 = t6/9
			paths.append(3)
		else:
			x = x-3
			u6 = u6-7
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		t6 = u6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))