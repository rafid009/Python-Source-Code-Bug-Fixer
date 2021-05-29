import numpy as np 

def function(x):

	t1 = x
	r1 = 8
	x = 1
	paths = []
	try:
		if t1 < 3:
			x = x*9
			paths.append(1)
		else:
			r1 = r1-t1
			t1 = 0+t1
			paths.append(2)
		if t1 <= 4:
			x = 3*x
			t1 = t1-1
			paths.append(3)
		else:
			x = 9/x
			r1 = t1/t1
			x = 1*1
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