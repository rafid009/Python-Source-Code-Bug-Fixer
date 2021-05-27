import numpy as np 

def function(x):

	o4 = 8
	t7 = x
	paths = []
	try:
		if o4 >= 9:
			o4 = 9/6
			paths.append(1)
		else:
			o4 = o4*t7
			x = x-o4
			o4 = 5/o4
			paths.append(2)
		if o4 < 1:
			o4 = o4-t7
			o4 = t7*t7
			paths.append(3)
		else:
			x = x*0
			t7 = o4/1
			x = x/1
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))