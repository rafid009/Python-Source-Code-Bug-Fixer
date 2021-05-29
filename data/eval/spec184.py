import numpy as np 

def function(x):

	t2 = 1
	o0 = 4
	paths = []
	try:
		if x < 5:
			o0 = t2*o0
			t2 = t2/4
			paths.append(1)
		else:
			o0 = o0*4
			t2 = t2+7
			t2 = t2*6
			paths.append(2)
		if t2 > 4:
			t2 = t2*8
			t2 = t2+x
			paths.append(3)
		else:
			o0 = o0-t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))