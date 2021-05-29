import numpy as np 

def function(x):

	t6 = x
	u6 = 2
	x = x
	paths = []
	try:
		if u6 <= 8:
			x = x+8
			x = x-9
			t6 = t6-u6
			paths.append(1)
		else:
			u6 = t6-7
			x = x+0
			u6 = 5-u6
			paths.append(2)
		if x >= 3:
			t6 = 5*9
			x = u6+x
			paths.append(3)
		else:
			u6 = u6+4
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))