import numpy as np 

def function(x):

	t2 = 0
	o8 = 9
	paths = []
	try:
		if t2 > 2:
			t2 = x*t2
			t2 = t2+t2
			o8 = 8/9
			paths.append(1)
		else:
			o8 = o8/3
			t2 = x-3
			x = t2-t2
			paths.append(2)
		if o8 <= 7:
			x = t2+x
			o8 = t2/6
			o8 = o8-o8
			paths.append(3)
		else:
			x = 0+x
			t2 = t2+8
			o8 = o8+t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))