import numpy as np 

def function(x):

	o4 = 3
	t4 = 0
	paths = []
	try:
		if x > 4:
			o4 = o4-8
			t4 = t4/3
			x = 1-x
			paths.append(1)
		else:
			t4 = 8+x
			paths.append(2)
		if t4 <= 8:
			t4 = o4/9
			o4 = x*o4
			t4 = t4/x
			paths.append(3)
		else:
			o4 = o4/2
			o4 = o4*8
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))