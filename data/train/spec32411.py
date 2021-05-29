import numpy as np 

def function(x):

	u1 = x
	t5 = 6
	paths = []
	try:
		if x <= 7:
			u1 = 6+u1
			t5 = 1/u1
			u1 = 0*u1
			paths.append(1)
		else:
			u1 = t5+u1
			t5 = 1+7
			x = 6*4
			paths.append(2)
		if x >= 5:
			u1 = u1*u1
			paths.append(3)
		else:
			u1 = 0+8
			t5 = t5+2
			u1 = 3*u1
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))