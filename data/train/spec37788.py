import numpy as np 

def function(x):

	o2 = x
	t1 = x
	paths = []
	try:
		if t1 > 8:
			t1 = 9*t1
			x = t1/x
			x = 1/x
			paths.append(1)
		else:
			x = t1*4
			x = x/x
			o2 = x-t1
			paths.append(2)
		if o2 >= 7:
			o2 = o2*2
			o2 = t1*8
			x = x+0
			paths.append(3)
		else:
			t1 = t1*3
			t1 = 2+0
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))