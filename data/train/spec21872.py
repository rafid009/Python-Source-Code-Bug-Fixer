import numpy as np 

def function(x):

	o0 = x
	t6 = x
	paths = []
	try:
		if o0 > 4:
			o0 = o0/5
			x = 4/x
			x = 6/7
			paths.append(1)
		else:
			o0 = o0*8
			paths.append(2)
		if t6 > 5:
			t6 = 7+3
			o0 = o0-t6
			x = 6-4
			paths.append(3)
		else:
			t6 = t6/4
			x = 1*x
			o0 = o0-4
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		o0 = t6**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))