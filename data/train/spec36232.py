import numpy as np 

def function(x):

	o3 = 5
	t9 = x
	paths = []
	try:
		if o3 <= 1:
			x = x/x
			x = x+0
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if t9 > 1:
			t9 = 7+t9
			paths.append(3)
		else:
			o3 = o3*o3
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		o3 = t9**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))