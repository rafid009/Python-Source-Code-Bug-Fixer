import numpy as np 

def function(x):

	t6 = 0
	o0 = 7
	paths = []
	try:
		if x <= 0:
			o0 = o0-x
			x = 4/x
			o0 = o0*9
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if t6 <= 1:
			o0 = 5+t6
			t6 = t6-o0
			paths.append(3)
		else:
			x = 2*x
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