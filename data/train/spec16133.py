import numpy as np 

def function(x):

	o0 = x
	t7 = 5
	paths = []
	try:
		if o0 > 6:
			o0 = o0+3
			t7 = o0+x
			o0 = o0*o0
			paths.append(1)
		else:
			t7 = 9-o0
			x = x+4
			t7 = t7/6
			paths.append(2)
		if x <= 7:
			x = x/1
			paths.append(3)
		else:
			x = x*9
			t7 = 5-x
			t7 = t7*8
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