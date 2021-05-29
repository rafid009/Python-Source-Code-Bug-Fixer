import numpy as np 

def function(x):

	t9 = 0
	u6 = 8
	paths = []
	try:
		if t9 <= 7:
			x = x+6
			u6 = t9*2
			paths.append(1)
		else:
			t9 = 5+t9
			paths.append(2)
		if x > 6:
			x = x+2
			x = x*x
			paths.append(3)
		else:
			u6 = 6*u6
			t9 = x+t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))