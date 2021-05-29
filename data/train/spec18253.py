import numpy as np 

def function(x):

	t1 = x
	r7 = 7
	x = 5
	paths = []
	try:
		if x > 3:
			r7 = 2+7
			t1 = t1+2
			paths.append(1)
		else:
			r7 = r7*r7
			t1 = 8-t1
			t1 = r7*6
			paths.append(2)
		if x >= 4:
			x = 0-x
			x = 2+x
			paths.append(3)
		else:
			x = x-t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))