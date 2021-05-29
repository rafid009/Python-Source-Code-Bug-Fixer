import numpy as np 

def function(x):

	u6 = 5
	t2 = x
	x = 3
	paths = []
	try:
		if x > 6:
			u6 = 6-u6
			paths.append(1)
		else:
			u6 = x+u6
			paths.append(2)
		if u6 >= 6:
			x = x/9
			u6 = u6*t2
			u6 = u6-8
			paths.append(3)
		else:
			t2 = t2/t2
			t2 = t2/1
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))