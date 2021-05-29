import numpy as np 

def function(x):

	u6 = 7
	t4 = 7
	paths = []
	try:
		if t4 < 1:
			t4 = 1+u6
			u6 = u6+2
			paths.append(1)
		else:
			x = x/3
			x = 0+x
			u6 = x+u6
			paths.append(2)
		if u6 <= 1:
			u6 = u6+u6
			t4 = 4-t4
			paths.append(3)
		else:
			t4 = x+x
			x = x/1
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