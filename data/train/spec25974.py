import numpy as np 

def function(x):

	o4 = 3
	t3 = 4
	paths = []
	try:
		if t3 > 9:
			x = x/o4
			o4 = 2*o4
			paths.append(1)
		else:
			t3 = 8*1
			t3 = 2-4
			paths.append(2)
		if o4 < 9:
			o4 = o4+2
			x = 4*4
			paths.append(3)
		else:
			o4 = o4*9
			o4 = o4-t3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))