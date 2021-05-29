import numpy as np 

def function(x):

	t2 = 8
	u6 = x
	paths = []
	try:
		if u6 >= 3:
			t2 = t2+t2
			paths.append(1)
		else:
			t2 = u6-t2
			u6 = u6-5
			x = x+t2
			paths.append(2)
		if t2 <= 3:
			u6 = 3*6
			paths.append(3)
		else:
			u6 = u6*4
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))